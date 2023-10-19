.. pharmacy documentation master file, created by
   sphinx-quickstart on Sat Apr 30 23:42:56 2022.
   version 0.2.0

.. _source: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html
.. https://stackoverflow.com/questions/59903051/sphinxs-autodocs-automodule-having-apparently-no-effect

.. meta::
   :description: pharmacy Module Documentation
   :keywords: python, pharmacy, sql, medicine, medical, apha, ashp, ichp, pharmacist, technician, doctor, hospital

Welcome to the *pharmacy* module documentation.
=====================================

.. toctree::
   :maxdepth: 2
   :caption: :

   ndc
   standardcolumnnames

The *pharmacy* module is intended to be a selection of utilities, classes and APIs intended to make pharmacy and healthcare data analytics easier.
Quickly compare prices, pull live data about drugs from OpenFDA and perform complex fuzzy matches with little code.

-----------------------------------
General Pattern - Read First
-----------------------------------
..  comment

#. Load source data into pandas DataFrames

#. Rename columns as the appropriate :doc:`Standard Column Names <standardcolumnnames>`.

   a. Most project time is spent here but be **patient** and **accurate**.
      Ensure that source columns match the definitions in :doc:`Standard Column Names <standardcolumnnames>`.
   b. Columns do not need to be renamed if they will not be part of the operations that
      the user wants to perform.

.. hint:: It is important to jump in and start working with real data.
          Avoid the urge to standardize every single column title.
          Have some fun with the data!






Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


