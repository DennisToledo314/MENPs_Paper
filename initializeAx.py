from brian2 import *


def my_axon(axon_morpho, eqs, membrane_c, axial_rho, g_na_f, g_na_p, g_k, g_l_node, g_l_inter,
            inter_c, const_potentials):

    myelinated_axon = SpatialNeuron(morphology=axon_morpho, model=eqs, Cm=membrane_c, Ri=axial_rho,
                                    method='exponential_euler', namespace=const_potentials)

    myelinated_axon.v = 'ER'

    myelinated_axon.main.gNaf = g_na_f
    myelinated_axon.main.gNap = g_na_p
    myelinated_axon.main.gK = g_k
    myelinated_axon.main.gL = g_l_node

    myelinated_axon.i1.gNaf = 0
    myelinated_axon.i1.gNap = 0
    myelinated_axon.i1.gK = 0
    myelinated_axon.i1.gL = g_l_inter
    myelinated_axon.i1.Cm = inter_c

    myelinated_axon.i1.n2.gNaf = g_na_f
    myelinated_axon.i1.n2.gNap = g_na_p
    myelinated_axon.i1.n2.gK = g_k
    myelinated_axon.i1.n2.gL = g_l_node

    myelinated_axon.i1.n2.i2.gNaf = 0
    myelinated_axon.i1.n2.i2.gNap = 0
    myelinated_axon.i1.n2.i2.gK = 0
    myelinated_axon.i1.n2.i2.gL = g_l_inter
    myelinated_axon.i1.n2.i2.Cm = inter_c

    myelinated_axon.i1.n2.i2.n3.gNaf = g_na_f
    myelinated_axon.i1.n2.i2.n3.gNap = g_na_p
    myelinated_axon.i1.n2.i2.n3.gK = g_k
    myelinated_axon.i1.n2.i2.n3.gL = g_l_node

    myelinated_axon.i1.n2.i2.n3.i3.gNaf = 0
    myelinated_axon.i1.n2.i2.n3.i3.gNap = 0
    myelinated_axon.i1.n2.i2.n3.i3.gK = 0
    myelinated_axon.i1.n2.i2.n3.i3.gL = g_l_inter
    myelinated_axon.i1.n2.i2.n3.i3.Cm = inter_c

    myelinated_axon.i1.n2.i2.n3.i3.n4.gNaf = g_na_f
    myelinated_axon.i1.n2.i2.n3.i3.n4.gNap = g_na_p
    myelinated_axon.i1.n2.i2.n3.i3.n4.gK = g_k
    myelinated_axon.i1.n2.i2.n3.i3.n4.gL = g_l_node

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.gNaf = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.gNap = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.gK = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.gL = g_l_inter
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.Cm = inter_c

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.gNaf = g_na_f
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.gNap = g_na_p
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.gK = g_k
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.gL = g_l_node

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.gNaf = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.gNap = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.gK = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.gL = g_l_inter
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.Cm = inter_c

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.gNaf = g_na_f
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.gNap = g_na_p
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.gK = g_k
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.gL = g_l_node

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.gNaf = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.gNap = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.gK = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.gL = g_l_inter
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.Cm = inter_c

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.gNaf = g_na_f
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.gNap = g_na_p
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.gK = g_k
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.gL = g_l_node

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.gNaf = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.gNap = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.gK = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.gL = g_l_inter
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.Cm = inter_c

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.gNaf = g_na_f
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.gNap = g_na_p
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.gK = g_k
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.gL = g_l_node

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.gNaf = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.gNap = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.gK = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.gL = g_l_inter
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.Cm = inter_c

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.gNaf = g_na_f
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.gNap = g_na_p
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.gK = g_k
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.gL = g_l_node

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.gNaf = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.gNap = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.gK = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.gL = g_l_inter
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.Cm = inter_c

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.gNaf = g_na_f
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.gNap = g_na_p
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.gK = g_k
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.gL = g_l_node

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.gNaf = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.gNap = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.gK = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.gL = g_l_inter
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.Cm = inter_c

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.gNaf = g_na_f
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.gNap = g_na_p
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.gK = g_k
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.gL = g_l_node

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.gNaf = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.gNap = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.gK = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.gL = g_l_inter
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.Cm = inter_c

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.gNaf = g_na_f
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.gNap = g_na_p
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.gK = g_k
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.gL = g_l_node

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.gNaf = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.gNap = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.gK = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.gL = g_l_inter
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.Cm = inter_c

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.gNaf = g_na_f
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.gNap = g_na_p
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.gK = g_k
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.gL = g_l_node

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.gNaf = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.gNap = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.gK = 0
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.gL = g_l_inter
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.Cm = inter_c

    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.gNaf = g_na_f
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.gNap = g_na_p
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.gK = g_k
    myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.gL = g_l_node

    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14
     .i14.gNaf) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14
     .i14.gNap) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14
     .i14.gK) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14
     .i14.gL) = g_l_inter
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14
     .i14.Cm) = inter_c

    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14
     .i14.n15.gNaf) = g_na_f
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14
     .i14.n15.gNap) = g_na_p
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14
     .i14.n15.gK) = g_k
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14
     .i14.n15.gL) = g_l_node

    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14
     .i14.n15.i15.gNaf) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14
     .i14.n15.i15.gNap) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14
     .i14.n15.i15.gK) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14
     .i14.n15.i15.gL) = g_l_inter
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14
     .i14.n15.i15.Cm) = inter_c

    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.gNaf) = g_na_f
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.gNap) = g_na_p
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.gK) = g_k
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.gL) = g_l_node

    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.gNaf) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.gNap) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.gK) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.gL) = g_l_inter
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.Cm) = inter_c

    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.gNaf) = g_na_f
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.gNap) = g_na_p
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.gK) = g_k
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.gL) = g_l_node

    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.gNaf) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.gNap) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.gK) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.gL) = g_l_inter
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.Cm) = inter_c

    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.gNaf) = g_na_f
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.gNap) = g_na_p
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.gK) = g_k
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.gL) = g_l_node

    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.gNaf) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.gNap) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.gK) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.gL) = g_l_inter
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.Cm) = inter_c

    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.gNaf) = g_na_f
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.gNap) = g_na_p
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.gK) = g_k
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.gL) = g_l_node

    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.gNaf) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.gNap) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.gK) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.gL) = g_l_inter
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.Cm) = inter_c

    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.n20.gNaf) = g_na_f
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.n20.gNap) = g_na_p
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.n20.gK) = g_k
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.n20.gL) = g_l_node

    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.n20.i20.gNaf) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.n20.i20.gNap) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.n20.i20.gK) = 0
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.n20.i20.gL) = g_l_inter
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.n20.i20.Cm) = inter_c

    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.n20.i20.n21.gNaf) = g_na_f
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.n20.i20.n21.gNap) = g_na_p
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.n20.i20.n21.gK) = g_k
    (myelinated_axon.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15.i15
     .n16.i16.n17.i17.n18.i18.n19.i19.n20.i20.n21.gL) = g_l_node

    return myelinated_axon
