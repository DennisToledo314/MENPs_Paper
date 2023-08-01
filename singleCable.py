from brian2 import *


def ax_morpho(node_diam, node_length, internode_diam, internode_length):
    axon_morpho = Cylinder(diameter=node_diam, length=node_length)

    axon_morpho.i1 = Cylinder(diameter=internode_diam, length=internode_length)

    axon_morpho.i1.n2 = Cylinder(diameter=node_diam, length=node_length)

    axon_morpho.i1.n2.i2 = Cylinder(diameter=internode_diam, length=internode_length)

    axon_morpho.i1.n2.i2.n3 = Cylinder(diameter=node_diam, length=node_length)

    axon_morpho.i1.n2.i2.n3.i3 = Cylinder(diameter=internode_diam, length=internode_length)

    axon_morpho.i1.n2.i2.n3.i3.n4 = Cylinder(diameter=node_diam, length=node_length)

    axon_morpho.i1.n2.i2.n3.i3.n4.i4 = Cylinder(diameter=internode_diam, length=internode_length)

    axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5 = Cylinder(diameter=node_diam, length=node_length)

    axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5 = Cylinder(diameter=internode_diam, length=internode_length)

    axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6 = Cylinder(diameter=node_diam, length=node_length)

    axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6 = Cylinder(diameter=internode_diam, length=internode_length)

    axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7 = Cylinder(diameter=node_diam, length=node_length)

    axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7 = Cylinder(diameter=internode_diam, length=internode_length)

    axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8 = Cylinder(diameter=node_diam, length=node_length)

    axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8 = Cylinder(diameter=internode_diam, length=internode_length)

    axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9 = Cylinder(diameter=node_diam, length=node_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9
     .i9) = Cylinder(diameter=internode_diam, length=internode_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9
     .i9.n10) = Cylinder(diameter=node_diam, length=node_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9
     .i9.n10.i10) = Cylinder(diameter=internode_diam, length=internode_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9
     .i9.n10.i10.n11) = Cylinder(diameter=node_diam, length=node_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9
     .i9.n10.i10.n11.i11) = Cylinder(diameter=internode_diam, length=internode_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9
     .i9.n10.i10.n11.i11.n12) = Cylinder(diameter=node_diam, length=node_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9
     .i9.n10.i10.n11.i11.n12.i12) = Cylinder(diameter=internode_diam, length=internode_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9
     .i9.n10.i10.n11.i11.n12.i12.n13) = Cylinder(diameter=node_diam, length=node_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9
     .i9.n10.i10.n11.i11.n12.i12.n13.i13) = Cylinder(diameter=internode_diam, length=internode_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9
     .i9.n10.i10.n11.i11.n12.i12.n13.i13.n14) = Cylinder(diameter=node_diam, length=node_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9
     .i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14) = Cylinder(diameter=internode_diam, length=internode_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9
     .n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15) = Cylinder(diameter=node_diam, length=node_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15
     .i15) = Cylinder(diameter=internode_diam, length=internode_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15
     .i15.n16) = Cylinder(diameter=node_diam, length=node_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15
     .i15.n16.i16) = Cylinder(diameter=internode_diam, length=internode_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15
     .i15.n16.i16.n17) = Cylinder(diameter=node_diam, length=node_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15
     .i15.n16.i16.n17.i17) = Cylinder(diameter=internode_diam, length=internode_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15
     .i15.n16.i16.n17.i17.n18) = Cylinder(diameter=node_diam, length=node_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15
     .i15.n16.i16.n17.i17.n18.i18) = Cylinder(diameter=internode_diam, length=internode_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15
     .i15.n16.i16.n17.i17.n18.i18.n19) = Cylinder(diameter=node_diam, length=node_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15
     .i15.n16.i16.n17.i17.n18.i18.n19.i19) = Cylinder(diameter=internode_diam, length=internode_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15
     .i15.n16.i16.n17.i17.n18.i18.n19.i19.n20) = Cylinder(diameter=node_diam, length=node_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15
     .i15.n16.i16.n17.i17.n18.i18.n19.i19.n20.i20) = Cylinder(diameter=internode_diam, length=internode_length)

    (axon_morpho.i1.n2.i2.n3.i3.n4.i4.n5.i5.n6.i6.n7.i7.n8.i8.n9.i9.n10.i10.n11.i11.n12.i12.n13.i13.n14.i14.n15
     .i15.n16.i16.n17.i17.n18.i18.n19.i19.n20.i20.n21) = Cylinder(diameter=node_diam, length=node_length)

    return axon_morpho
