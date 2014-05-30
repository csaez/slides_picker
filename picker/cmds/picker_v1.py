from maya import cmds  # importamos los comandos de maya


w = cmds.window(title="Picker", width=300)  # nueva vtana
cmds.columnLayout(adjustableColumn=True)  # layout vertical
cmds.text(label="char: mario_rig", height=30)  # etiqueta

# ZONA CENTRAL
color = (0.9, 0.7, 0.1)  # amarillo
cmds.button(label="Eyes", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_cn_lookAt"))
cmds.button(label="Head", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_cn_head"))
cmds.button(label="Neck", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_cn_neck"))
cmds.button(label="Chest", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_cn_chest"))

color = (0.6, 0.06, 0.01)  # rojo oscuro
cmds.button(label="SpineFK2", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_cn_spineFK2"))
cmds.button(label="SpineFK1", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_cn_spineFK1"))

color = (0.9, 0.7, 0.1)  # amarillo
cmds.button(label="Pelvis", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_cn_pelvis"))

color = (0.98, 0.58, 0.43)  # rosa
cmds.button(label="Upper Body", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_cn_upperbody"))

# IZQUIERDA
color = (0.1, 0.4, 0.6)  # azul
cmds.button(label="Clavicle Left", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_lf_clavicle"))
cmds.button(label="ShoulderFK Left", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_lf_shoulderFK"))
cmds.button(label="ElbowFK Left", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_lf_elbowFK"))
cmds.button(label="HandFK Left", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_lf_handFK"))
cmds.button(label="LegPole Left", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_lf_legPole"))
cmds.button(label="FootIK Left", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_lf_footIK"))

# DERECHA
color = (0.8, 0.15, 0.15)  # rojo
cmds.button(label="Clavicle Right", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_rt_clavicle"))
cmds.button(label="ShoulderFK Right", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_rt_shoulderFK"))
cmds.button(label="ElbowFK Right", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_rt_elbowFK"))
cmds.button(label="HandFK Right", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_rt_handFK"))
cmds.button(label="LegPole Right", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_rt_legPole"))
cmds.button(label="FootIK Right", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_rt_footIK"))

# BASE
color = (0.98, 0.58, 0.43)  # rosa
cmds.button(label="Base", height=30, backgroundColor=color,
            command=lambda _: cmds.select("mario_rig:mario_ac_cn_base"))

# SELECCIONAR TODO
anims = ("mario_rig:mario_ac_lf_kneeIK", "mario_rig:mario_ac_lf_lowleg_bend",
         "mario_rig:mario_ac_lf_upleg_bend", "mario_rig:mario_ac_rt_kneeIK",
         "mario_rig:mario_ac_rt_lowleg_bend", "mario_rig:mario_ac_rt_upleg_bend",
         "mario_rig:mario_ac_cn_midbody_bend", "mario_rig:mario_ac_cn_lowbody_bend",
         "mario_rig:mario_ac_cn_topbody_bend", "mario_rig:mario_ac_cn_upperteeth",
         "mario_rig:mario_ac_lf_eye", "mario_rig:mario_ac_rt_eye",
         "mario_rig:mario_edit_cn_nosetip", "mario_rig:mario_edit_cn_bottomhead",
         "mario_rig:mario_edit_cn_middownhead", "mario_rig:mario_edit_cn_midnose",
         "mario_rig:mario_edit_lf_ear", "mario_rig:mario_edit_rt_ear",
         "mario_rig:mario_edit_rt_eye", "mario_rig:mario_edit_cn_topnose",
         "mario_rig:mario_edit_lf_eye", "mario_rig:mario_edit_cn_midtophead",
         "mario_rig:mario_edit_cn_tophead", "mario_rig:mario_ac_cn_lowerteeth",
         "mario_rig:mario_ac_cn_tongue_5", "mario_rig:mario_ac_cn_tongue_4",
         "mario_rig:mario_ac_cn_tongue_3", "mario_rig:mario_ac_cn_tongue_2",
         "mario_rig:mario_ac_cn_tongue_1", "mario_rig:mario_ac_lf_forearm_bend",
         "mario_rig:mario_ac_lf_arm_bend", "mario_rig:mario_ac_rt_forearm_bend",
         "mario_rig:mario_ac_rt_arm_bend", "mario_rig:mario_ac_lf_index3",
         "mario_rig:mario_ac_lf_index2", "mario_rig:mario_ac_lf_index1",
         "mario_rig:mario_ac_lf_index0", "mario_rig:mario_ac_lf_middle3",
         "mario_rig:mario_ac_lf_middle2", "mario_rig:mario_ac_lf_middle1",
         "mario_rig:mario_ac_lf_middle0", "mario_rig:mario_ac_lf_ring3",
         "mario_rig:mario_ac_lf_ring2", "mario_rig:mario_ac_lf_ring1",
         "mario_rig:mario_ac_lf_ring0", "mario_rig:mario_ac_lf_pinkey3",
         "mario_rig:mario_ac_lf_pinkey2", "mario_rig:mario_ac_lf_pinkey1",
         "mario_rig:mario_ac_lf_pinkey0", "mario_rig:mario_ac_lf_thumb3",
         "mario_rig:mario_ac_lf_thumb2", "mario_rig:mario_ac_lf_thumb1",
         "mario_rig:mario_ac_rt_index3", "mario_rig:mario_ac_rt_index2",
         "mario_rig:mario_ac_rt_index1", "mario_rig:mario_ac_rt_index0",
         "mario_rig:mario_ac_rt_middle3", "mario_rig:mario_ac_rt_middle2",
         "mario_rig:mario_ac_rt_middle1", "mario_rig:mario_ac_rt_middle0",
         "mario_rig:mario_ac_rt_ring3", "mario_rig:mario_ac_rt_ring2",
         "mario_rig:mario_ac_rt_ring1", "mario_rig:mario_ac_rt_ring0",
         "mario_rig:mario_ac_rt_pinkey3", "mario_rig:mario_ac_rt_pinkey2",
         "mario_rig:mario_ac_rt_pinkey1", "mario_rig:mario_ac_rt_pinkey0",
         "mario_rig:mario_ac_rt_thumb3", "mario_rig:mario_ac_rt_thumb2",
         "mario_rig:mario_ac_rt_thumb1", "mario_rig:mario_ac_lf_elbow_bend",
         "mario_rig:mario_ac_rt_elbow_bend", "mario_rig:mario_ac_lf_knee_bend",
         "mario_rig:mario_ac_rt_knee_bend", "mario_rig:mario_ac_cn_head",
         "mario_rig:mario_ac_cn_neck", "mario_rig:mario_ac_cn_base",
         "mario_rig:mario_ac_cn_spineFK1", "mario_rig:mario_ac_cn_spineFK2",
         "mario_rig:mario_ac_cn_pelvis", "mario_rig:mario_ac_cn_chest",
         "mario_rig:mario_ac_lf_clavicle", "mario_rig:mario_ac_rt_clavicle",
         "mario_rig:mario_ac_cn_upperbody", "mario_rig:mario_ac_lf_shoulderFK",
         "mario_rig:mario_ac_lf_elbowFK", "mario_rig:mario_ac_lf_handFK",
         "mario_rig:mario_ac_rt_shoulderFK", "mario_rig:mario_ac_rt_elbowFK",
         "mario_rig:mario_ac_rt_handFK", "mario_rig:mario_ac_lf_toe",
         "mario_rig:mario_ac_rt_toe", "mario_rig:mario_ac_lf_arm_settings",
         "mario_rig:mario_ac_rt_arm_settings", "mario_rig:mario_ac_lf_leg_settings",
         "mario_rig:mario_ac_rt_leg_settings", "mario_rig:mario_ac_lf_footIK",
         "mario_rig:mario_ac_rt_footIK", "mario_rig:mario_ac_lf_legPole",
         "mario_rig:mario_ac_rt_legPole", "mario_rig:mario_ac_cn_lookAt",
         "mario_rig:mario_ac_cn_jaw")

cmds.button(l="All", height=30, nbg=True, c=lambda _: cmds.select(anims))

# abrimos la ventana
cmds.showWindow(w)
