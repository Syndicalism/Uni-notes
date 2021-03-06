---
aliases: ["golden rules of negative feedback op amps"]
tags: ["Question","QFormat3"]
---

#### Describe
## Negative feedback and operational amplifiers

You get some usefull behaviour when you use negative feedback with an [[operational amplifier]]:
![[Pasted image 20220419150913.png]]
Initially the voltage at $V_{+}$ would make $V_{out}$ spike to a really high value (usually createing a square wave as seen in [[operational amplifier#Generating square waves]]) but in this case since $V_{out}$ feeds back to $V_{-}$ you get the following set of equations:
$$\begin{align*}
V_{out} &= A_{OL}(V_{+}-V_{-}) & V_{-} = V_{out}\\
V_{out} &= A_{OL}(V_{+}-V_{out})\\
V_{out} + A_{OL}V_{out} &= A_{OL}V_{+}\\
V_{out} &= V_{+} \frac{A_{OL}}{1+A_{OL}}\\
V_{out} &= V_{+} \frac{1}{\frac{1}{A_{OL}}+1}\\
&& A_{OL} &>100000\\
V_{out} &\approx V_{+}
\end{align*}$$
Since $A_{OL}$ is so large we can basically assume that $V_{out}=V_{+}$, but whats more useful is the further implications of this; $V_{out}$ will equal whatever is nessisary to make $V_{-}\approx V_{+}$ which forms the basis of the golden rules of negative feedback op amps:

- The output voltage will become whatever value is nessisary to make the voltage difference between the inputs zero
- No current flows between the two inputs