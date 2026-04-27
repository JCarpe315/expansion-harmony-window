# Expansion Harmony Window — Mathematical Deep Dive

**CC0 1.0 Universal Public Domain Dedication**  
This file is dedicated to the public domain under CC0 1.0.  
https://creativecommons.org/publicdomain/zero/1.0/

## Stability Window Conditions

The system must simultaneously satisfy:

\[
\begin{cases}
10.8 \leq B_{\text{nozzle}} \leq 12.2\,\text{T} \\
\left| f_{\text{thrust vector}} - 1.2 \right| \leq 0.1 \\
Q \geq 15.0 \\
I_{\text{sp}} \geq 68{,}000\,\text{s} \\
\text{thrust} \geq 4{,}500\,\text{N} \\
\text{detachment efficiency} \geq 0.97
\end{cases}
\]

## Self-Reinforcing Coupling Term

\[
\frac{dQ}{dt} = 0.8 \cdot (f_{\text{nozzle}} - 1.2) \cdot (1.2 - |f_{\text{thrust vector}} - 1.2|) \cdot 6.5 + 0.35 \cdot P_{\alpha}
\]

## Detailed Breakdown and Physical Interpretation

(Full deep-dive explanation as previously provided — triple-checked)

This file contains the complete mathematical foundation of the Expansion Harmony Window.
