---
aliases: ["max flow velocity in laminar flow in a pipe","flow velocity in laminar flow in a pipe"]
tags: ["Question","QFormat3"]
---

#### Describe the method for
## Modeling laminar flow in a pipe
### Usefull equation bit
The shear stress decreases linearly while the velocity increases linearly:
![[Pasted image 20220426171348.png]]

The equation describing the flow formed is
> ### $$ U = - \frac{R^{2}}{4\mu} \frac{dp}{dx} \left(1-\left(\frac{r}{R}\right)^{2}\right) $$ 
> ### $$ U_{max} = - \frac{R^{2}}{4\mu} \frac{dp}{dx} $$ 
> ### $$ \frac{U}{U_{max}} = \left(1-\left(\frac{r}{R}\right)^{2}\right) $$
>> where:
>> $U=$ Flow velocity
>> $U_{max}=$ Max flow velocity
>> $R=$ Pipe radius
>> $\mu=$ [[shear viscosity of the fluid]]
>> $p=$ pressure
>> $x=$ displacement along the pipe in the direction of flow
>> $r=$ distance from centre of the pipe

> ### $$ \bar{U} = \frac{U_{max}}{2} $$ 
>> where:
>> $\bar{U}=$ [[bulk velocity]]
>> $U_{max}=$ [[modeling laminar flow in a pipe|max flow velocity in laminar flow in a pipe]]

### Derivation
[[UNFINISHED STUFF|come back and do derivation]]
<!--- 
We make some assumptions: 
- flow is fully developed (so it's cross section/flow is uniform for its length, aka a really long pipe) so no [[boundary layer]] [[first meme since easter break lets go|shinanigins]].
- Flow is incompressible
- No mass accumulation (flow rate is constant for the length of the pipe)

![[Pasted image 20220426154544.png]]

First equation is us expressing the net force acting on the section of water, and since acceleration is zero we know that net force is zero. So pressure force equals pipe surface shear force:

$$\begin{align*}
( (p+dp) - p ) \times \pi R^{2} &= \tau_{w} \times 2R\pi dx\\
dpR &= 2 \tau_{w} dx \\
\frac{dp}{dx} \frac{R}{2} &= \tau_{w}
\end{align*}$$

Next we need to derive an equation for modelling shear inside the pipe cross section, here we can also use force balencing:
![[Pasted image 20220426165153.png]]
$$\begin{align*}
\tau &= (R-r) \tau_{w}
\end{align*}$$

Now we have an expression relating the shear force and rate of change of pressure. Next we can model this as a [[newtonian fluids|newtonian fluid]] and get [[newtonian fluids#^998109|this equation]]:
$$\begin{align*}
\tau &= \mu dU & \tau &= (R-r) \tau_{w} & \frac{dp}{dx} \frac{R}{2} &= \tau_{w}\\
&&  &= (R-r) \frac{dp}{dx} \frac{R}{2}\\
(R-r) \frac{dp}{dx} \frac{R}{2} &= \mu dU\\
(R-r) \frac{dp}{dx} \frac{R}{2} &= \mu dU
\end{align*}$$
-->