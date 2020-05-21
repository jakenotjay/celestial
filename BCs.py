#Solar System:
m_S = 1.99E30
m_E = 5.97E24
m_M = 7.35E22
m_merc = 0.330E24
m_ven = 4.87E24
m_mars = 0.642E24
m_jupiter = 1898E24
m_saturn = 568E24
m_uranus = 86.8E24
m_neptune = 102E24
m_pluto = 0.0146E24
G = 6.67408E-11

labels = ['Sun', 'Earth', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
m_N = [m_S, m_E, m_M, m_merc, m_ven, m_mars, m_jupiter, m_saturn, m_uranus, m_neptune, m_pluto]
# sun xy
r_N[0, 0, 0] = 0
r_N[0, 0, 1] = 0
# earth xy
r_N[1, 0, 0] = 1.06E11
r_N[1, 0, 1] = 1.06E11
# moon xy
r_N[2, 0, 0] = 1.06E11 + 272E6
r_N[2, 0, 1] = 1.06E11 + 272E6
# mercury xy
r_N[3, 0, 0] = 4.09E10
r_N[3, 0, 1] = 4.09E10
# venus xy
r_N[4, 0, 0] = 7.65E10
r_N[4, 0, 1] = 7.65E10
# mars xy
r_N[5, 0, 0] = 1.61E11
r_N[5, 0, 1] = 1.61E11
# jupiter xy
r_N[6, 0, 0] = 5.51E11
r_N[6, 0, 1] = 5.51E11
# saturn xy
r_N[7, 0, 0] = 1.01E12
r_N[7, 0, 1] = 1.01E12
# uranus xy
r_N[8, 0, 0] = 2.03E12
r_N[8, 0, 1] = 2.03E12
# neptune xy
r_N[9, 0, 0] = 3.18E12
r_N[9, 0, 1] = 3.18E12
# pluto xy
r_N[10, 0, 0] = 4.18E12
r_N[10, 0, 1] = 4.18E12

#sun xy velocity
v_N[0, 0, 0] = 0
v_N[0, 0, 1] = 0
#earth xy velocity
v_N[1, 0, 0] = +21125.3
v_N[1, 0, 1] = -21125.3
#moon xy velocity
v_N[2, 0, 0] = 21125.3 + 724.2
v_N[2, 0, 1] = -(21125.3 + 724.2)
#mercury xy velocity
v_N[3, 0, 0] = 33516.9
v_N[3, 0, 1] = -33516.8
#venus xy velocity
v_N[4, 0, 0] = 24748.7
v_N[4, 0, 1] = -24748.7
#mars xy velocity
v_N[5, 0, 0] = 17041.3
v_N[5, 0, 1] = -17041.3
#jupiter xy velocity
v_N[6, 0, 0] = 9263.1
v_N[6, 0, 1] = -9263.1
#saturn xy velocity
v_N[7, 0, 0] = 6858.9
v_N[7, 0, 1] = -6858.9
#uranus xy velocity
v_N[8, 0, 0] = 4808.3
v_N[8, 0, 1] = -4808.3
#neptune xy velocity
v_N[9, 0, 0] = 3818.4
v_N[9, 0, 1] = -3818.4
#pluto xy velocity
v_N[10, 0, 0] = 3323.4
v_N[10, 0, 1] = -3323.4

#Fo8:
G = 1
labels = ['Body 1', 'Body 2', 'Body 3']
m_N = [1, 1, 1]

r_N[0, 0, 0] = -0.97000436
r_N[0, 0, 1] = 0.24308753

r_N[1, 0, 0] = 0
r_N[1, 0, 1] = 0

r_N[2, 0, 0] = 0.97000436
r_N[2, 0, 1] = -0.24308753

v_N[0, 0, 0] = 0.4662036850
v_N[0, 0, 1] = 0.4323657300

v_N[1, 0, 0] = -0.93240737
v_N[1, 0, 1] = -0.86473146

v_N[2, 0, 0] = 0.4662036850
v_N[2, 0, 1] = 0.4323657300


#Fo84:
G = 1
labels = ['Body 1', 'Body 2', 'Body 3', 'Body 4']
m_N = [1, 1, 1, 1]

r_N[0, 0, 0] = -0.97000436
r_N[0, 0, 1] = 0.24308753

r_N[1, 0, 0] = 0
r_N[1, 0, 1] = 0

r_N[2, 0, 0] = 0.97000436
r_N[2, 0, 1] = -0.24308753

r_N[3, 0, 0] = 2
r_N[3, 0, 1] = -10

v_N[0, 0, 0] = 0.4662036850
v_N[0, 0, 1] = 0.4323657300

v_N[1, 0, 0] = -0.93240737
v_N[1, 0, 1] = -0.86473146

v_N[2, 0, 0] = 0.4662036850
v_N[2, 0, 1] = 0.4323657300

v_N[3, 0, 0] = 0
v_N[3, 0, 1] = 1