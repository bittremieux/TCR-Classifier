A computational approach to determine CD8+ T-cell receptor characteristics underlying peptide recognition
=========================================================================================================

Current T-cell epitope prediction tools are a valuable resource in designing targeted immunogenicity experiments. They typically focus on, and are able to, accurately predict peptide binding and presentation by major histocompatibility complex (MHC) molecules on the surface of antigen-presenting cells. However, recognition of the peptide-MHC complex by a T-cell receptor (TCR) is often not included in these tools. We developed a classification approach based on random forest classifiers to predict recognition of a peptide by a T-cell receptor and discover patterns that contribute to recognition. We considered two approaches to solve this problem: (1) distinguishing between two sets of TCRs that each bind to a known peptide and (2) retrieving TCRs that bind to a given peptide from a large pool of TCRs. Evaluation of the models on two HIV-1, B*08-restricted epitopes reveals good performance and hints towards structural CDR3 features that can determine peptide immunogenicity. These results are of particular importance as they show that prediction of T-cell epitope and T-cell epitope recognition based on sequence data is a feasible approach. In addition, the validity of our models not only serves as a proof of concept for the prediction of immunogenic T-cell epitopes but also paves the way for more general and high performing models.

Dependencies
------------

* boruta
* IPython
* joblib
* matplotlib
* numpy
* pandas
* seaborn
* pyteomics
* skbio
* sklearn

Contact
-------

Nicolas De Neuter

nicolas.deneuter(at)uantwerpen.be

University of Antwerp

ADReM/biomina
