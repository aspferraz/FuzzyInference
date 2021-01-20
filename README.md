# FuzzyInference

Example of a fuzzy system for determining the internal pressure inside a boiler as a function of its internal temperature and the volume of water inside it.

<br><b>Input Variables:</b><br>
• Temperature: ranges from 800<sup>o</sup>C to 1200<sup>o</sup>C.<br>
• Volume: varies from 2m<sup>3</sup> to 12m<sup>3</sup> of water.<br>

<br><b>Output Variable:</b><br>
• Pressure: ranges from 4 atm to 12 atm.

The set of fuzzy rules is given by the following sentences:
<br>Rule 1: If (Temperature is Low) and (Volume is Small)
So (pressure is low)
<br>Rule 2: If (Temperature is Medium) and (Volume is Small)
So (pressure is low)
<br>Rule 3: If (Temperature is High) and (Volume is Small)
So (Pressure is Average)
<br>Rule 4: If (Temperature is Low) and (Volume is Average)
So (pressure is low)
<br>Rule 5: If (Temperature is Average) and (Volume is Average)
So (Pressure is Average)
<br>Rule 6: If (Temperature is High) and (Volume is Average)
So (pressure is high)
<br>Rule 7: If (Temperature is Low) and (Volume is Large)
So (Pressure is Average)
<br>Rule 8: If (Temperature is Medium) and (Volume is Large)
So (pressure is high)
<br>Rule 9: If (Temperature is High) and (Volume is Large)
So (pressure is high)
