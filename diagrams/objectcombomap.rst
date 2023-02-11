- https://www.john-cd.com/cheatsheets/Markup_and_Documentation/reStructuredText/
- https://mermaid-js.github.io/mermaid/#/./n00b-syntaxReference

Object Combo Map
===================

Intoduction
------------------------

pypharm allows users to take in Excel, CSV and SQL data sources and combine them with ease to create advanced analysis products.  Often end users in the pharmacy / medicine community do not have access to the database so pypharm is designed with the goal of allowing users to export a file or two from any software and create any output.



Combination Map
------------------------------


```mermaid
graph LR
    %% First two levels
    rx[Prescriptions] --> rxf[Prescriptions and Fills]
    f[Fills] --> rxf
    pt[Patient Demographics] --> rxpt[Rxs with Demographics]
    rx --> rxpt
    ins[Insurance Info] --> fins[Fills with Detailed Ins]
    f --> fins
    f --> fderivedschedule>Derived Schedule]
    emp[Employee Data] -.-> fderivedschedule

    %% Third level

    fins --> fins_app>Sort by Medicaid]
    rxpt --> rxpt_app>Map of Patient Volume]
    md[Doctor Info] --> mdrx[Rxs with Doctor Info]
    rx --> mdrx

    f --> f_app>Fill analysis]
    pc[Price Catalog] --> rxpc>Alternative Pricing]
    rx --> rxpc

    %%subgraph one
    %%    graph LR
    %%        x --> y
    %%    end


%% Combos
    rx -. + Operator puts files together .-> rx

%%

%% Styling

    classDef source fill:#00d,stroke:#008,stroke-width:2px,color:#000;
    classDef combo fill:#0dd,stroke:#088,stroke-width:2px,color:#000;
    classDef product fill:#d00,stroke:#800,stroke-width:2px,color:#000;
    class rx,f,pt,ins,md,pc,emp source;
    class rxf,fins,rxpt,mdrx combo;
    class fins_app,rxpt_app,f_app,rxpc,fderivedschedule product;

```


The '+' Operator for Source Files
-----------------
The pycharm workflow for source files is as follows:

