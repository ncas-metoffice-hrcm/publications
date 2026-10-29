# Simple script to produce a stacked bar chart of publications for HRCM, annotated with key projects.
# NB, for simplicity, "EERIE.bib" includes km-scale work (DYAMOND, nextGEMS etc) that could be separated in future.
#
# Author: Alexander J. Baker


from pybtex import database
import operator
import numpy as np
from collections import OrderedDict
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


class PublicationGroup:
    def __init__(self,filename,label,colour,xy,annotation):
        self.filename = filename
        self.label = label
        self.colour = colour
        self.xy = xy
        self.annotation = annotation


def parse_file(filename):
    """ Parse a bibtex file and return fields for bar plot """
    yeard = {}
    filename = './bib/'+filename
    print(filename)
    bdata = database.parse_file(filename)
    for entry in bdata.entries:
        field = bdata.entries[entry].fields
        year = int(field['year'])
        if year not in yeard:
            yeard[year] = 0
        yeard[year] += 1
        
    ordered = sorted(yeard.items(), key=operator.itemgetter(0))
    years = [k[0] for k in ordered]
    counts = [k[1] for k in ordered]

    return years, counts


def get_counts(groups):
    """ Get counts per bib file """
    filenames = [group.filename for group in groups]

    y_dict = OrderedDict()
    n_dict = OrderedDict()    
    keys = list()
    for fn in filenames:
        key = fn.rsplit('_')[0]
        keys.append(key)
        y, n = parse_file(fn)
        y_dict[key] = y
        n_dict[key] = n
    years_cat = list()
    for key in keys:
        years_cat = years_cat + y_dict[key]
    years_set = set(years_cat)
    #years_set = set([y_dict[key] for key in keys])
    years_all = range(min(years_set), max(years_set) + 1)

    counts_dict = OrderedDict()
    for key in keys:
        counts_dict[key] = []
        for yr in years_all:
            if yr in y_dict[key]:
                counts_dict[key].append(n_dict[key][y_dict[key].index(yr)])
            else:
                counts_dict[key].append(0)
    #print(counts_dict)

    return years_all, counts_dict


def plot_stacked_bar(years_all,counts_dict):
    """ Plot stacked bars """
    colours = [group.colour for group in groups]
    labels = [group.label for group in groups]
    bottom = np.zeros(len(years_all))
    for key in list(counts_dict.keys()):
        idx = list(counts_dict.keys()).index(key)
        plt.bar(years_all, counts_dict[key], width=0.75, color=colours[idx], edgecolor='k', bottom=bottom)
        bottom += np.array(counts_dict[key])
    plt.bar(years_all, bottom, width=0.75, color=colours[idx], fill=False, edgecolor='k')


def format_plot(groups,years_all,title,fig_fn):
    """ Format and annotate plot """
    font_annotations = {'fontfamily':'sans-serif', 'fontsize':'10'}
    font_title = {'fontfamily':'sans-serif', 'fontsize':'11','fontweight':'bold'}
    #plt.rcParams["font.sans-serif"] = ["Helvetica"]

    plt.xticks(np.arange(years_all[0], years_all[-1],4), fontsize=11)
    plt.yticks(np.arange(0, 35, 5), fontsize=11)
    plt.ylim(0, 30)
    plt.ylabel('# publications', fontsize=11)
    for s in ['top','right']:
        plt.gca().spines[s].set_visible(False)
    plt.title(title, **font_title)

    colours = [group.colour for group in groups]
    labels = [group.label for group in groups]
    handles = [(Patch(facecolor = c,edgecolor = 'k',label = l))\
        for c,l in zip(colours,labels)]
    plt.legend(handles = handles, prop = dict(size=10,weight='bold'), loc='upper left', frameon = False)
    
    for group in groups:
        plt.annotate(group.annotation, xy=group.xy, xycoords='data', color=group.colour, **font_annotations)

    print(fig_fn)
    plt.savefig('./figures/' + fig_fn)
    plt.show()
    

if __name__ == "__main__":

    core = PublicationGroup('HRCM_core.bib','Core','grey',(2003, 2),
        'Period of\nmodel\ndevelopment\n'+r'2004$-$2008')
    ujcc = PublicationGroup('UJCC.bib','UJCC','firebrick',(2004, 9),
        'UK'+'$-$'+'Japan Climate\nCollaboration (UJCC)\nEarth Simulator\n'+r'2005$-$2007')
    upscale = PublicationGroup('UPSCALE.bib','UPSCALE','dodgerblue',(2009, 16),
        'UPSCALE\nPRACE\n'+r'2012$-$2016')
    primavera = PublicationGroup('PRIMAVERA.bib','PRIMAVERA','darkblue',(2017, 19),
        'PRIMAVERA\nHorizon-2020\n'+r'2016$-$2020')
    eerie = PublicationGroup('EERIE.bib','Towards km-scale','darkorange',(2018, 24),
        'Towards km-scale\n(DYAMOND, EERIE,\nHighResMIP2, nextGEMS)\n'+r'2021$-$')

    groups = [core,ujcc,upscale,primavera,eerie]

    title = 'HRCM publications'
    fig_fn = 'hrcm_publications_2026.pdf'

    years_all,counts_dict = get_counts(groups)
    plot_stacked_bar(years_all,counts_dict)
    format_plot(groups,years_all,title,fig_fn)

