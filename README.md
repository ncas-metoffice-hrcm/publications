# publications
This repo contains categorised bibliographical data for all peer-reviewed publications from HRCM, and a script to visualise publications over time.

**All new publications should be added to the relevant `.bib` file, listed below.**  

The `.bib` files in this repo are used to generate a public, searchable publications list at [**hrcm.ceda.ac.uk/publications**](https://hrcm.ceda.ac.uk/publications/). After adding a publication here, in `BibTeX` format, run the "Update publications" workflow at the HRCM website repo ([cedadev/hrcm-website](https://github.com/cedadev/hrcm-website/tree/main)). New `.bib` files (e.g., for new projects, consortia) may be created in `bib/`.  

#### `.bib/`

**`bib/EERIE.bib`**  
Publications from EERIE, the successor project to PRIMAVERA, and related km-scale modelling work (e.g., nextGEMS, DYAMOND, HighResMIP). This will likely be broken into multiple files km-scale work progresses.  
**`bib/HRCM_core.bib`**  
Publications covering Met Office model development and underpinning capability.  
**`bib/PRIMAVERA.bib`**  
Publications from CMIP6-HighResMIP and PRIMAVERA, the project that coordinated the European contribution.  
**`bib/UJCC.bib`**  
Publications from the UK–Japan Climate Collaboration, covering early model-development using the Earth Simulator.  
**`bib/UPSCALE.bib`**  
Publications from the UPSCALE project on resolution sensitivity using the Unified Model.  
**`bib/unclassified.bib`**  
Papers with (currently) no defined project link.  

#### `simple_pybib.py`  
Plot categorised, stacked bar chart of HRCM publications over time and save in `figures/`. Any new or renamed `.bib` files must be updated in `simple_pybib.py` — see the `PublicationGroup()` class.  
