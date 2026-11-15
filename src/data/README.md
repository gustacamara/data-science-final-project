# Data

## DTHHRDY: death classification

The `DTHHRDY` column in `GTEx_Analysis_v11_Annotations_SubjectPhenotypesDS.txt` describes how each donor died, following the 4-point Hardy Scale. The GTEx team also added a fifth category, 0, for donors who were on a ventilator right before death.

| Value | Category | What it means |
|---|---|---|
| 0 | Ventilator case | The donor was on a ventilator immediately before death. |
| 1 | Violent and fast death | Death caused by an accident, blunt force trauma or suicide, with a terminal phase estimated at less than 10 minutes. |
| 2 | Fast death of natural causes | Sudden and unexpected death of someone who was reasonably healthy, with a terminal phase estimated at less than 1 hour. A heart attack is the typical example. |
| 3 | Intermediate death | Death after a terminal phase of 1 to 24 hours that doesn't fit categories 2 or 4. The person was ill, but the death was unexpected. |
| 4 | Slow death | Death after a long illness, with a terminal phase longer than 1 day, commonly cancer or chronic lung disease. The death was not unexpected. |

Keep in mind that 19 donors have no value in this column. Because of these gaps, pandas reads it as a float, so the values show up as `0.0`, `1.0` and so on.
