.. pypharm documentation master file, created by
   sphinx-quickstart on Sat Apr 30 23:42:56 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. _source: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html

.. meta::
   :description: pypharm Documentation
   :keywords: python, pharmacy, sql, medicine, medical, apha, ashp

Welcome to the pypharm documentation.
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

pypharm is a selection of utilities, classes and APIs intended to make pharmacy and healthcare data analytics easier.
Quickly compare prices, pull live data about drugs from OpenFDA and perform complex fuzzy matches with little code.

-----------------------------------
General Pattern - Must Read
-----------------------------------
..  comment

#. Load source data into pandas DataFrames

#. Rename columns as the appropriate `Standard Column Names`.

   #. Most project time is spent here but be patient and accurate.
      Ensure that source columns match the definitions in `Standard Column Names`.
   #. Columns do not need to be renamed if they will not be part of the operations that
      the user wants to perform.

.. hint:: It is important to jump in and start working with real data.
          Avoid the urge to change every single column title.  Have some fun with the data!


#.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`