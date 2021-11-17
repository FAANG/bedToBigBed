# bedToBigBed

This is a Python script to convert BED files to BigBed format, used by the UCSC Genome Browser.

At the moment, this script works specifically for the CAGE track files as it takes into consideration it's format.

### To run the script:

 **python main.py <dir_path>** where dir_apth is the path of the directory containing the list of BED files.

The original BED files submitted to us (_novel_CAGE_ and _annot_CAGE_) do not abide to the UCSC rules for BED format and
therefore several changes were made to the files before they could be converted to BigBed.

The the conversion script is run on the directory path, 2 sub-directories are created in the _dir_path._

Those 2 sub-directpries are namely: **_updated_** and **_bigbed_**

**1) updated directory**

This folder contains the modified bed files which abide to the UCSC rules for BED files format.

The changes made are:

- inclusion of the _name_ field.  "." is used since the _name_ field has not been provided and is thus considered empty.
- moving the _width_ column to the end because it’s a non-standard user-defined column and needs to be after all other BED fields
- swapping the order of _score_ and _strand_ to abide to BED fields ordering
- removal of headers
- editing the _chromEnd_ value from 16617 to 16616 because of error message thrown by the **bedToBigBed** application. The _chromEnd_ value provided by our submitter is _16617_ while the value of the _chromEnd_ size for _NC_001941.1_ is _16616_. See chrom.sizes file **CF_002742125.1_Oar_rambouillet_v1.0.chrom.sizes**
- _score_ value must be between 0 and 1000. _Score_ was therefore changed to int and where the value is greater than 1000, only the first 3 digits are considered as score - assuming that the decimal point was misplaced by our submitter.
- an autosql file is used to describe the fields and include the non-standard fields to ensure that conversion to bigBed happens seamlessly


**2) bigbed**

This folder contains the successfully generated bigBed files, ready to be uploaded to UCSC.


