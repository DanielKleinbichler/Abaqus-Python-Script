from abaqus import *
from abaqusConstants import *
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
Mdb() 

#------------------------------------------------------------------------
# Parameters (In reference to global CSYS)
#------------------------------------------------------------------------
Width = 56.18 #x-dimension
Length = Width  #z-dimension
Thickness = 3.09
Height = 50 # y-dimension

Youngs = 4797.25
Poisson = 0.4

mesh_factor = 45

#------------------------------------------------------------------------
# Bottom Part Creation
#------------------------------------------------------------------------
sketch_bottom = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1000.0)

geometry_bottom = sketch_bottom.geometry 
vertices_bottom = sketch_bottom.vertices
dimensions_bottom = sketch_bottom.dimensions
constraints_bottom = sketch_bottom.constraints

sketch_bottom.setPrimaryObject(option=STANDALONE)

sketch_bottom.rectangle(point1=(0.0, 0.0), point2=(Width, Length))

part_bottom = mdb.models['Model-1'].Part(name='Bottom', dimensionality=THREE_D, type=DEFORMABLE_BODY)

part_bottom.BaseSolidExtrude(sketch=sketch_bottom, depth=Thickness)

sketch_bottom.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']

#------------------------------------------------------------------------
# Wall_X Part Creation
#------------------------------------------------------------------------
sketch_Wall_X = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1000.0)

geometry_Wall_X = sketch_Wall_X.geometry
vertices_Wall_X = sketch_Wall_X.vertices
dimensions_Wall_X = sketch_Wall_X.dimensions
constraints_Wall_X = sketch_Wall_X.constraints

sketch_Wall_X.setPrimaryObject(option=STANDALONE)

sketch_Wall_X.rectangle(point1=(0.0, 0.0), point2=(Width, Height))
part_Wall_X = mdb.models['Model-1'].Part(name='Wall_X', dimensionality=THREE_D, type=DEFORMABLE_BODY)

part_Wall_X.BaseSolidExtrude(sketch=sketch_Wall_X, depth=Thickness)

sketch_Wall_X.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']

datums_Wall_X = part_Wall_X.datums
cells_Wall_X = part_Wall_X.cells
P_vertices_Wall_X = part_Wall_X.vertices

#------------------------------------------------------------------------
# First edge
#------------------------------------------------------------------------
faces_Wall_X = part_Wall_X.faces
edges_Wall_X = part_Wall_X.edges

transform_Edge1X = part_Wall_X.MakeSketchTransform(
    sketchPlane = faces_Wall_X[1], 
    sketchUpEdge = edges_Wall_X[6], 
    sketchPlaneSide = SIDE1, 
    sketchOrientation = RIGHT, 
    origin = (0.0, Height, 0.0) 
) 

sketch_Edge1X = mdb.models['Model-1'].ConstrainedSketch(
    name='__profile__', 
    sheetSize=1000, 
    gridSpacing=5, 
    transform= transform_Edge1X
) 

geometry_Edge1X = sketch_Edge1X.geometry
vertices_Edge1X = sketch_Edge1X.vertices
dimensions_Edge1X = sketch_Edge1X.dimensions
constraints_Edge1X = sketch_Edge1X.constraints

sketch_Edge1X.setPrimaryObject(option=SUPERIMPOSE)

part_Wall_X.projectReferencesOntoSketch(sketch=sketch_Edge1X, filter=COPLANAR_EDGES)

sketch_Edge1X.Line(point1=(-20.0, 5.0), point2=(-10.0, 10.0))
sketch_Edge1X.CoincidentConstraint(entity1=vertices_Edge1X[4], entity2=vertices_Edge1X[2])
sketch_Edge1X.CoincidentConstraint(entity1=vertices_Edge1X[5], entity2=vertices_Edge1X[0])

sketch_Edge1X.Line(point1=(-20.0, 5.0), point2=(-10.0, 10.0))
sketch_Edge1X.CoincidentConstraint(entity1=vertices_Edge1X[6], entity2=vertices_Edge1X[5])

sketch_Edge1X.Line(point1=(-20.0, 5.0), point2=(-10.0, 10.0))
sketch_Edge1X.CoincidentConstraint(entity1=vertices_Edge1X[8], entity2=vertices_Edge1X[4])
sketch_Edge1X.CoincidentConstraint(entity1=vertices_Edge1X[9], entity2=vertices_Edge1X[7])

sketch_Edge1X.AngularDimension(
    line1=geometry_Edge1X[8], 
    line2=geometry_Edge1X[5], 
    textPoint=(5.0, 5.0), 
    value=45.0
)

sketch_Edge1X.ParallelConstraint(entity1=geometry_Edge1X[7], entity2=geometry_Edge1X[2])

part_Wall_X.CutExtrude(
    sketchPlane = faces_Wall_X[1], 
    sketchUpEdge = edges_Wall_X[6], 
    sketchPlaneSide = SIDE1, 
    sketchOrientation = RIGHT, 
    sketch = sketch_Edge1X,
    flipExtrudeDirection = OFF
)

sketch_Edge1X.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']

#------------------------------------------------------------------------
# Second edge
#------------------------------------------------------------------------

transform_Edge2X = part_Wall_X.MakeSketchTransform(
    sketchPlane = faces_Wall_X[2], 
    sketchUpEdge = edges_Wall_X[7], 
    sketchPlaneSide = SIDE1, 
    sketchOrientation = RIGHT, 
    origin = (Width, 0.0, 0.0) 
) 

sketch_Edge2X = mdb.models['Model-1'].ConstrainedSketch(
    name='__profile__', 
    sheetSize = 1000, 
    gridSpacing = 5, 
    transform = transform_Edge2X
)

geometry_Edge2X = sketch_Edge2X.geometry
vertices_Edge2X = sketch_Edge2X.vertices
dimensions_Edge2X = sketch_Edge2X.dimensions
constraints_Edge2X = sketch_Edge2X.constraints

sketch_Edge2X.setPrimaryObject(option=SUPERIMPOSE)

part_Wall_X.projectReferencesOntoSketch(sketch = sketch_Edge2X, filter=COPLANAR_EDGES)

sketch_Edge2X.Line(point1=(-20.0, 5.0), point2=(-10.0, 10.0))
sketch_Edge2X.CoincidentConstraint(entity1=vertices_Edge2X[4], entity2=vertices_Edge2X[2])
sketch_Edge2X.CoincidentConstraint(entity1=vertices_Edge2X[5], entity2=vertices_Edge2X[3])

sketch_Edge2X.Line(point1=(-20.0, 5.0), point2=(-10.0, 10.0))
sketch_Edge2X.CoincidentConstraint(entity1=vertices_Edge2X[6], entity2=vertices_Edge2X[5])

sketch_Edge2X.Line(point1=(-20.0, 5.0), point2=(-10.0, 10.0))
sketch_Edge2X.CoincidentConstraint(entity1=vertices_Edge2X[8], entity2=vertices_Edge2X[4])
sketch_Edge2X.CoincidentConstraint(entity1=vertices_Edge2X[9], entity2=vertices_Edge2X[7])

sketch_Edge2X.AngularDimension(
    line1=geometry_Edge2X[8], 
    line2=geometry_Edge2X[5], 
    textPoint=(5.0, 5.0), 
    value=45.0
)

sketch_Edge2X.ParallelConstraint(entity1=geometry_Edge2X[7], entity2=geometry_Edge2X[4])

part_Wall_X.CutExtrude(
    sketchPlane=faces_Wall_X[2], 
    sketchUpEdge=edges_Wall_X[7], 
    sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, 
    sketch=sketch_Edge2X, 
    flipExtrudeDirection=OFF
)

sketch_Edge2X.unsetPrimaryObject()

#------------------------------------------------------------------------
# Wall_Z part creation
#------------------------------------------------------------------------

sketch_Wall_Z = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1000.0)

geometry_Wall_Z = sketch_Wall_Z.geometry
vertices_Wall_Z = sketch_Wall_Z.vertices
dimensions_Wall_Z = sketch_Wall_Z.dimensions
constraints_Wall_Z = sketch_Wall_Z.constraints

sketch_Wall_Z.setPrimaryObject(option=STANDALONE) 

sketch_Wall_Z.rectangle(point1=(0.0, 0.0), point2=(Length, Height)) 

part_Wall_Z = mdb.models['Model-1'].Part(
    name='Wall_Z', 
    dimensionality=THREE_D, 
    type=DEFORMABLE_BODY
)

part_Wall_Z.BaseSolidExtrude(sketch=sketch_Wall_Z, depth=Thickness)

sketch_Wall_Z.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']

datums_Wall_Z = part_Wall_Z.datums
cells_Wall_Z = part_Wall_Z.cells
P_vertices_Wall_Z = part_Wall_Z.vertices

#------------------------------------------------------------------------
# First edge
#------------------------------------------------------------------------
faces_Wall_Z = part_Wall_Z.faces
edges_Wall_Z = part_Wall_Z.edges

transform_Edge1Z = part_Wall_Z.MakeSketchTransform(
    sketchPlane = faces_Wall_Z[1], 
    sketchUpEdge = edges_Wall_Z[4], 
    sketchPlaneSide = SIDE1, 
    sketchOrientation = RIGHT, 
    origin=(0.0, Height, 0.0) 
)

sketch_Edge1Z = mdb.models['Model-1'].ConstrainedSketch(
    name='__profile__', 
    sheetSize = 285.65, 
    gridSpacing = 7.14, 
    transform = transform_Edge1Z
)

geometry_Edge1Z = sketch_Edge1Z.geometry
vertices_Edge1Z = sketch_Edge1Z.vertices
dimensions_Edge1Z = sketch_Edge1Z.dimensions
constraints_Edge1Z = sketch_Edge1Z.constraints

sketch_Edge1Z.setPrimaryObject(option=SUPERIMPOSE)

part_Wall_Z.projectReferencesOntoSketch(sketch = sketch_Edge1Z, filter=COPLANAR_EDGES)

sketch_Edge1Z.Line(point1=(-20.0, 5.0), point2=(-10.0, 10.0))
sketch_Edge1Z.CoincidentConstraint(entity1=vertices_Edge1Z[4], entity2=vertices_Edge1Z[2])
sketch_Edge1Z.CoincidentConstraint(entity1=vertices_Edge1Z[5], entity2=vertices_Edge1Z[0])

sketch_Edge1Z.Line(point1=(-20.0, 5.0), point2=(-10.0, 10.0))
sketch_Edge1Z.CoincidentConstraint(entity1=vertices_Edge1Z[6], entity2=vertices_Edge1Z[5])

sketch_Edge1Z.Line(point1=(-20.0, 5.0), point2=(-10.0, 10.0))
sketch_Edge1Z.CoincidentConstraint(entity1=vertices_Edge1Z[8], entity2=vertices_Edge1Z[4])
sketch_Edge1Z.CoincidentConstraint(entity1=vertices_Edge1Z[9], entity2=vertices_Edge1Z[7])

sketch_Edge1Z.AngularDimension(
    line1=geometry_Edge1Z[8], 
    line2=geometry_Edge1Z[5], 
    textPoint=(10.0, 10.0), 
    value=45.0
)

sketch_Edge1Z.ParallelConstraint(entity1=geometry_Edge1Z[7], entity2=geometry_Edge1Z[2])

part_Wall_Z.CutExtrude(
    sketchPlane=faces_Wall_Z[1], 
    sketchUpEdge=edges_Wall_Z[4], 
    sketchPlaneSide=SIDE1, 
    sketchOrientation=RIGHT, 
    sketch=sketch_Edge1Z, 
    flipExtrudeDirection=OFF
)

sketch_Edge1Z.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']

#------------------------------------------------------------------------
# Second edge
#------------------------------------------------------------------------

transform_Edge2Z = part_Wall_Z.MakeSketchTransform(
    sketchPlane = faces_Wall_Z[2], 
    sketchUpEdge = edges_Wall_Z[7], 
    sketchPlaneSide = SIDE1, 
    sketchOrientation = RIGHT, 
    origin=(Length, 0.0, 0.0) 
) 

sketch_Edge2Z = mdb.models['Model-1'].ConstrainedSketch(
    name='__profile__', 
    sheetSize = 285.65, 
    gridSpacing = 7.14, 
    transform = transform_Edge2Z
)

geometry_Edge2Z = sketch_Edge2Z.geometry
vertices_Edge2Z = sketch_Edge2Z.vertices
dimensions_Edge2Z = sketch_Edge2Z.dimensions
constraints_Edge2Z = sketch_Edge2Z.constraints

sketch_Edge2Z.setPrimaryObject(option=SUPERIMPOSE)

part_Wall_Z.projectReferencesOntoSketch(sketch = sketch_Edge2Z, filter=COPLANAR_EDGES)

sketch_Edge2Z.Line(point1=(-20.0, 5.0), point2=(-10.0, 10.0))
sketch_Edge2Z.CoincidentConstraint(entity1=vertices_Edge2Z[4], entity2=vertices_Edge2Z[2])
sketch_Edge2Z.CoincidentConstraint(entity1=vertices_Edge2Z[5], entity2=vertices_Edge2Z[3])

sketch_Edge2Z.Line(point1=(-20.0, 5.0), point2=(-10.0, 10.0))
sketch_Edge2Z.CoincidentConstraint(entity1=vertices_Edge2Z[6], entity2=vertices_Edge2Z[5])

sketch_Edge2Z.Line(point1=(-20.0, 5.0), point2=(-10.0, 10.0))
sketch_Edge2Z.CoincidentConstraint(entity1=vertices_Edge2Z[8], entity2=vertices_Edge2Z[4])
sketch_Edge2Z.CoincidentConstraint(entity1=vertices_Edge2Z[9], entity2=vertices_Edge2Z[7])

sketch_Edge2Z.AngularDimension(
    line1=geometry_Edge2Z[8], 
    line2=geometry_Edge2Z[5], 
    textPoint=(10.0, 10.0), 
    value=45.0
)

sketch_Edge2Z.ParallelConstraint(entity1=geometry_Edge2Z[7], entity2=geometry_Edge2Z[4])

part_Wall_Z.CutExtrude(
    sketchPlane = faces_Wall_Z[2], 
    sketchUpEdge = edges_Wall_Z[7], 
    sketchPlaneSide = SIDE1, 
    sketchOrientation = RIGHT, 
    sketch = sketch_Edge2Z, 
    flipExtrudeDirection = OFF
)

sketch_Edge2Z.unsetPrimaryObject()
del mdb.models['Model-1'].sketches['__profile__']

#------------------------------------------------------------------------
# Creating the assembly
#------------------------------------------------------------------------
assembly = mdb.models['Model-1'].rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)

assembly.Instance(name='Bottom', part=part_bottom, dependent=ON)
assembly.Instance(name='Wall_X', part=part_Wall_X, dependent=ON)
assembly.Instance(name='Wall_Z', part=part_Wall_Z, dependent=ON)

assembly.rotate(
    instanceList=('Bottom', ), 
    axisPoint=(0.0, 0.0, 0.0), 
    axisDirection=(1.0, 0.0, 0.0), 
    angle=90.0
)
assembly.rotate(
    instanceList=('Wall_Z', ), 
    axisPoint=(0.0, 0.0, 0.0), 
    axisDirection=(0.0, 1.0, 0.0), 
    angle=90.0
)
assembly.translate(
    instanceList=('Wall_Z', ), 
    vector=(0.0, 0.0, Length)
)
assembly.DatumCsysByThreePoints(
    name='Local CSYS', 
    coordSysType=CARTESIAN, 
    origin=(Width/2, (Height+2*Thickness)/2, Length/2), 
    point1=(Width, (Height+2*Thickness)/2, Length/2), 
    point2=(Width/2, Height+2*Thickness, Length/2)
)
assembly.RadialInstancePattern(
    instanceList=('Wall_Z', ), 
    point=(Width/2, (Height+2*Thickness)/2, Length/2), 
    axis=(0.0, 1.0, 0.0), 
    number=2, 
    totalAngle=360.0
)
assembly.RadialInstancePattern(
    instanceList=('Wall_X', ), 
    point=(Width/2, (Height+2*Thickness)/2, Length/2), 
    axis=(0.0, 1.0, 0.0), 
    number=2, 
    totalAngle=360.0
)
assembly.LinearInstancePattern(
    instanceList=('Bottom', ), 
    direction1=(0.0, 1.0, 0.0), 
    direction2=(0.0, 1.0, 0.0),
    number1=2, 
    number2=1,  
    spacing1=Height+Thickness, 
    spacing2=50.0 
)

mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='Wall_X-rad-2', toName='Wall_X-Mirrored')
mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='Bottom-lin-2-1', toName='Top')
mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='Wall_Z-rad-2', toName='Wall_Z-Mirrored')

Bottom_Walls_Face = assembly.Set(
    name = 'Bottom_Walls_Face',
    faces = assembly.instances['Bottom'].faces.findAt(((Width/2.0, 0.0, Length/2.0),))
)
Walls_Bottom_FaceX = assembly.Set(
    name = 'Walls_Bottom_FaceX',
    faces = assembly.instances['Wall_X'].faces.findAt(((Width/2.0, 0.0, Thickness/2.0),))
)
Walls_Bottom_FaceXMir = assembly.Set(
    name = 'Walls_Bottom_FaceXMir',
    faces = assembly.instances['Wall_X-Mirrored'].faces.findAt(((Width/2.0, 0.0, Length-(Thickness/2.0)),))
)
Walls_Bottom_FaceZ = assembly.Set(
    name = 'Walls_Bottom_FaceZ',
    faces = assembly.instances['Wall_Z'].faces.findAt(((Thickness/2.0, 0.0, Length/2.0),))
)
Walls_Bottom_FaceZMir = assembly.Set(
    name = 'Walls_Bottom_FaceZMir',
    faces = assembly.instances['Wall_Z-Mirrored'].faces.findAt(((Width-(Thickness/2.0), 0.0, Length/2.0),))
)

Top_Walls_Face = assembly.Set(
    name = 'Top_Walls_Face',
    faces = assembly.instances['Top'].faces.findAt(((Width/2.0, Height, Length/2.0),))
)
Walls_Top_FaceX = assembly.Set(
    name = 'Walls_Top_FaceX',
    faces = assembly.instances['Wall_X'].faces.findAt(((Width/2.0, Height, Thickness/2.0),))
)
Walls_Top_FaceXMir = assembly.Set(
    name = 'Walls_Top_FaceXMir',
    faces = assembly.instances['Wall_X-Mirrored'].faces.findAt(((Width/2.0, Height, Length-(Thickness/2.0)),))
)
Walls_Top_FaceZ = assembly.Set(
    name = 'Walls_Top_FaceZ',
    faces = assembly.instances['Wall_Z'].faces.findAt(((Thickness/2.0, Height, Length/2.0),))
)
Walls_Top_FaceZMir = assembly.Set(
    name = 'Walls_Top_FaceZMir',
    faces = assembly.instances['Wall_Z-Mirrored'].faces.findAt(((Width-(Thickness/2.0), Height, Length/2.0),))
)

Wall_X_Wall_Z_Face = assembly.Set(
    name = 'Wall_X_Wall_Z_Face',
    faces = assembly.instances['Wall_X'].faces.findAt(((Thickness/2.0, Height/2.0, Thickness/2.0),))
)
Wall_Z_Wall_X_Face = assembly.Set(
    name = 'Wall_Z_Wall_X_Face',
    faces = assembly.instances['Wall_Z'].faces.findAt(((Thickness/2.0, Height/2.0, Thickness/2.0),))
)

Wall_Z_Wall_XMir_Face = assembly.Set(
    name = 'Wall_Z_Wall_XMir_Face',
    faces = assembly.instances['Wall_Z'].faces.findAt(((Thickness/2.0, Height/2.0, Length-(Thickness/2.0)),))
)
Wall_XMir_Wall_Z_Face = assembly.Set(
    name = 'Wall_XMir_Wall_Z_Face',
    faces = assembly.instances['Wall_X-Mirrored'].faces.findAt(((Thickness/2.0, Height/2.0, Length-(Thickness/2.0)),))
)

Wall_XMir_Wall_ZMir_Face = assembly.Set(
    name = 'Wall_XMir_Wall_ZMir_Face',
    faces = assembly.instances['Wall_X-Mirrored'].faces.findAt(((Width-(Thickness/2.0), Height/2.0, Length-(Thickness/2.0)),))
)
Wall_ZMir_Wall_XMir_Face = assembly.Set(
    name = 'Wall_ZMir_Wall_XMir_Face',
    faces = assembly.instances['Wall_Z-Mirrored'].faces.findAt(((Width-(Thickness/2.0), Height/2.0, Length-(Thickness/2.0)),))
)

Wall_ZMir_Wall_X_Face = assembly.Set(
    name = 'Wall_ZMir_Wall_X_Face',
    faces = assembly.instances['Wall_Z-Mirrored'].faces.findAt(((Width-(Thickness/2.0), Height/2.0, Thickness/2.0),))
)
Wall_X_Wall_ZMir_Face = assembly.Set(
    name = 'Wall_X_Wall_ZMir_Face',
    faces = assembly.instances['Wall_X'].faces.findAt(((Width-(Thickness/2.0), Height/2.0, Thickness/2.0),))
)
#------------------------------------------------------------------------
# Material and Section Creation + Assignment
#------------------------------------------------------------------------

mdb.models['Model-1'].Material(name='Acrylic')
mdb.models['Model-1'].materials['Acrylic'].Elastic(table=((Youngs, Poisson), ))

mdb.models['Model-1'].HomogeneousSolidSection(
    name='Acrylic', 
    material='Acrylic', 
    thickness=None
)

def assign_section(part_name):
    assigned_part = mdb.models['Model-1'].parts[part_name]
    cells = assigned_part.cells.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(cells=cells)
    assigned_part.SectionAssignment(
        region = region,
        sectionName = 'Acrylic',
        offset = 0.0,
        offsetType = MIDDLE_SURFACE,
        offsetField = '',
        thicknessAssignment = FROM_SECTION
    )

assign_section(part_name='Bottom')
assign_section(part_name='Wall_X')
assign_section(part_name='Wall_Z')

#------------------------------------------------------------------------
# Defining the Pre-Contact and Loading Step
#------------------------------------------------------------------------

mdb.models['Model-1'].StaticStep(
    name='Pre-Contact', 
    previous='Initial', 
    initialInc=0.25, 
    nlgeom=ON
)

mdb.models['Model-1'].StaticStep(
    name='Loading', 
    previous='Pre-Contact', 
    initialInc=0.0015, 
    nlgeom=ON
)

#------------------------------------------------------------------------
# Interaction definitions
#------------------------------------------------------------------------


mdb.models['Model-1'].ContactProperty('Gasket')

mdb.models['Model-1'].interactionProperties['Gasket'].TangentialBehavior(
    formulation=PENALTY, 
    directionality=ISOTROPIC, 
    slipRateDependency=OFF, 
    pressureDependency=OFF, 
    temperatureDependency=OFF, 
    dependencies=0, 
    table=((0.8, ), ), 
    shearStressLimit=None, 
    maximumElasticSlip=FRACTION, 
    fraction=0.005, 
    elasticSlipStiffness=None
)

mdb.models['Model-1'].interactionProperties['Gasket'].NormalBehavior(
    pressureOverclosure=HARD, 
    allowSeparation=ON, 
    constraintEnforcementMethod=DEFAULT
)

#------------------------------------------------------------------------
# Interaction Assignments
#------------------------------------------------------------------------

Walls_Bottom = assembly.Surface(
    side1Faces = Walls_Bottom_FaceX.faces + Walls_Bottom_FaceXMir.faces + Walls_Bottom_FaceZ.faces + Walls_Bottom_FaceZMir.faces, 
    name='Walls-Bottom'
)
Bottom_Walls = assembly.Surface(
    side1Faces = Bottom_Walls_Face.faces, 
    name = 'Bottom-Walls'
)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(
    name='Bottom-Walls', 
    createStepName='Initial', 
    main = Bottom_Walls, 
    secondary = Walls_Bottom, 
    sliding=FINITE, 
    thickness=ON, 
    interactionProperty='Gasket', 
    adjustMethod=NONE, 
    initialClearance=OMIT, 
    datumAxis=None, 
    clearanceRegion=None
)

Walls_Top = assembly.Surface(
    side1Faces = Walls_Top_FaceX.faces + Walls_Top_FaceXMir.faces + Walls_Top_FaceZ.faces + Walls_Top_FaceZMir.faces, 
    name='Walls-Top'
)
Top_Walls = assembly.Surface(
    side1Faces = Top_Walls_Face.faces, 
    name = 'Top-Walls'
)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(
    name='Top-Walls', 
    createStepName='Initial', 
    main = Top_Walls, 
    secondary = Walls_Top, 
    sliding=FINITE, 
    thickness=ON, 
    interactionProperty='Gasket', 
    adjustMethod=NONE, 
    initialClearance=OMIT, 
    datumAxis=None, 
    clearanceRegion=None
)

Wall_X_Wall_Z = assembly.Surface(
    side1Faces = Wall_X_Wall_Z_Face.faces,
    name='Wall_X-Wall_Z'
)
Wall_Z_Wall_X = assembly.Surface(
    side1Faces = Wall_Z_Wall_X_Face.faces, 
    name = 'Wall_Z-Wall_X'
)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(
    name='Wall_X-Wall_Z', 
    createStepName='Initial', 
    main = Wall_X_Wall_Z, 
    secondary = Wall_Z_Wall_X, 
    sliding=FINITE, 
    thickness=ON, 
    interactionProperty='Gasket', 
    adjustMethod=NONE, 
    initialClearance=OMIT, 
    datumAxis=None, 
    clearanceRegion=None
)

Wall_Z_Wall_X_Mirrored = assembly.Surface(
    side1Faces = Wall_Z_Wall_XMir_Face.faces,
    name='Wall_Z-Wall_X-Mirrored'
)
Wall_X_Mirrored_Wall_Z = assembly.Surface(
    side1Faces = Wall_XMir_Wall_Z_Face.faces, 
    name = 'Wall_X-Mirrored-Wall_Z'
)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(
    name='Wall_Z-Wall_X-Mirrored', 
    createStepName='Initial', 
    main = Wall_Z_Wall_X_Mirrored, 
    secondary = Wall_X_Mirrored_Wall_Z, 
    sliding=FINITE, 
    thickness=ON, 
    interactionProperty='Gasket', 
    adjustMethod=NONE, 
    initialClearance=OMIT, 
    datumAxis=None, 
    clearanceRegion=None
)

Wall_X_Mirrored_Wall_Z_Mirrored = assembly.Surface(
    side1Faces = Wall_XMir_Wall_ZMir_Face.faces,
    name = 'Wall_X-Mirrored-Wall_Z-Mirrored'
)
Wall_Z_Mirrored_Wall_X_Mirrored = assembly.Surface(
    side1Faces = Wall_ZMir_Wall_XMir_Face.faces, 
    name = 'Wall_Z-Mirrored-Wall_X-Mirrored'
)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(
    name='Wall_X-Mirrored-Wall_Z-Mirrored', 
    createStepName='Initial', 
    main=Wall_X_Mirrored_Wall_Z_Mirrored, 
    secondary=Wall_Z_Mirrored_Wall_X_Mirrored, 
    sliding=FINITE, 
    thickness=ON, 
    interactionProperty='Gasket', 
    adjustMethod=NONE, 
    initialClearance=OMIT, 
    datumAxis=None, 
    clearanceRegion=None
)

Wall_Z_Mirrored_Wall_X = assembly.Surface(
    side1Faces = Wall_ZMir_Wall_X_Face.faces,
    name = 'Wall_Z-Mirrored-Wall_X'
)
Wall_X_Wall_Z_Mirrored = assembly.Surface(
    side1Faces = Wall_X_Wall_ZMir_Face.faces, 
    name = 'Wall_X-Wall_Z-Mirrored'
)
mdb.models['Model-1'].SurfaceToSurfaceContactStd(
    name='Wall_Z-Mirrored-Wall_X', 
    createStepName='Initial', 
    main=Wall_Z_Mirrored_Wall_X, 
    secondary=Wall_X_Wall_Z_Mirrored, 
    sliding=FINITE, 
    thickness=ON, 
    interactionProperty='Gasket', 
    adjustMethod=NONE, 
    initialClearance=OMIT, 
    datumAxis=None, 
    clearanceRegion=None
)

#------------------------------------------------------------------------
# Mesh Generation
#------------------------------------------------------------------------

part_Wall_X.DatumPlaneByThreePoints(
    point1=part_Wall_X.InterestingPoint(edge = edges_Wall_X[4], rule=MIDDLE), 
    point2=part_Wall_X.InterestingPoint(edge = edges_Wall_X[6], rule=MIDDLE), 
    point3=part_Wall_X.InterestingPoint(edge = edges_Wall_X[7], rule=MIDDLE)
)
part_Wall_X.DatumPlaneByOffset(
    plane = datums_Wall_X[5], 
    point = P_vertices_Wall_X[1]
)
partition1cells_Wall_X = cells_Wall_X.findAt(
    ((Width/2.0, Height/2.0, Thickness/2.0),)
)
part_Wall_X.PartitionCellByDatumPlane(
    datumPlane = datums_Wall_X[6], 
    cells = partition1cells_Wall_X
)

part_Wall_X.DatumPlaneByOffset(
    plane = datums_Wall_X[5], 
    point = P_vertices_Wall_X[9]
)
partition2cells_Wall_X = cells_Wall_X.findAt(
    ((Width/2.0, Height/2.0, Thickness/2.0),)
)
part_Wall_X.PartitionCellByDatumPlane(
    datumPlane = datums_Wall_X[8], 
    cells = partition2cells_Wall_X
)

part_Wall_Z.DatumPlaneByThreePoints(
    point1=part_Wall_Z.InterestingPoint(edge = edges_Wall_Z[6], rule = MIDDLE), 
    point2=part_Wall_Z.InterestingPoint(edge = edges_Wall_Z[4], rule = MIDDLE), 
    point3=part_Wall_Z.InterestingPoint(edge = edges_Wall_Z[7], rule = MIDDLE)
)
part_Wall_Z.DatumPlaneByOffset(
    plane = datums_Wall_Z[5], 
    point = P_vertices_Wall_Z[1]
)
partition1cells_Wall_Z = cells_Wall_Z.findAt(
    ((Width/2.0, Height/2.0, Thickness/2.0),)
)
part_Wall_Z.PartitionCellByDatumPlane(
    datumPlane = datums_Wall_Z[6], 
    cells = partition1cells_Wall_Z
)

part_Wall_Z.DatumPlaneByOffset(
    plane = datums_Wall_Z[5], 
    point = P_vertices_Wall_Z[9]
)
partition2cells_Wall_Z = cells_Wall_Z.findAt(
    ((Width/2.0, Height/2.0, Thickness/2.0),)
)
part_Wall_Z.PartitionCellByDatumPlane(
    datumPlane = datums_Wall_Z[8], 
    cells = partition2cells_Wall_Z
)

cells_bottom = part_bottom.cells.findAt(((0.0, 0.0, 0.0),))

part_bottom.seedPart(
    size=Length/mesh_factor, 
    deviationFactor=0.1, 
    minSizeFactor=0.1
)
part_bottom.setMeshControls(
    regions=cells_bottom, 
    technique=STRUCTURED,
    elemShape=HEX
)
elem_type_hex = mesh.ElemType(
    elemCode=C3D20R, 
    elemLibrary=STANDARD
)
part_bottom.setElementType(
    regions=(cells_bottom,),  
    elemTypes=(elem_type_hex,)
)
part_bottom.generateMesh()

meshEdge1X = part_Wall_X.cells.findAt(
    ((Thickness / 2.0, Height / 2.0, Thickness / 2.0),)
)
meshEdge2X = part_Wall_X.cells.findAt(
    ((Width - (Thickness / 2.0), Height / 2.0, Thickness / 2.0),)
)
part_Wall_X.setMeshControls(
    regions=meshEdge1X,
    elemShape=WEDGE,
    technique=SWEEP
)
part_Wall_X.setMeshControls(
    regions=meshEdge2X,
    elemShape=WEDGE,
    technique=SWEEP
)
elem_type_wedge = mesh.ElemType(
    elemCode = C3D15, 
    elemLibrary = STANDARD
)
part_Wall_X.setElementType(
    regions=(meshEdge1X,),
    elemTypes=(elem_type_wedge,)
)
part_Wall_X.setElementType(
    regions=(meshEdge2X,),
    elemTypes=(elem_type_wedge,)
)
hex_cells_WallX = part_Wall_X.cells.findAt(
    ((Width/2.0, Height / 2.0, Thickness / 2.0),)
)
part_Wall_X.setMeshControls(
    regions=hex_cells_WallX,
    elemShape=HEX,
    technique=STRUCTURED 
)
part_Wall_X.setElementType(
    regions=(hex_cells_WallX,),
    elemTypes=(elem_type_hex,)
)
part_Wall_X.seedPart(
    size=Length/mesh_factor,
    deviationFactor=0.1,
    minSizeFactor=0.1
)
part_Wall_X.generateMesh()

meshEdge1Z = cells_Wall_Z.findAt(
    ((Thickness/2.0, Height/2.0, Thickness/2.0),)
)
meshEdge2Z = cells_Wall_Z.findAt(
    ((Width-(Thickness/2.0), Height/2.0, Thickness/2.0),)
)
part_Wall_Z.setMeshControls(
    regions = meshEdge1Z, 
    elemShape = WEDGE, 
    technique = SWEEP
)
part_Wall_Z.setMeshControls(
    regions = meshEdge2Z, 
    elemShape = WEDGE, 
    technique = SWEEP
)
part_Wall_Z.setElementType(
    regions=(meshEdge1Z,),
    elemTypes=(elem_type_wedge,)
)
part_Wall_Z.setElementType(
    regions=(meshEdge2Z,),
    elemTypes=(elem_type_wedge,)
)
hex_cells_WallZ = part_Wall_Z.cells.findAt(
    ((Width/2.0, Height / 2.0, Thickness / 2.0),)
)
part_Wall_Z.setMeshControls(
    regions=hex_cells_WallZ,
    elemShape=HEX,
    technique=STRUCTURED 
)
part_Wall_Z.setElementType(
    regions=(hex_cells_WallZ,),
    elemTypes=(elem_type_hex,)
)
part_Wall_Z.seedPart(
    size = Length/mesh_factor, 
    deviationFactor = 0.1, 
    minSizeFactor = 0.1
) 
part_Wall_Z.generateMesh()

#------------------------------------------------------------------------
# Boundary Conditions
#------------------------------------------------------------------------

assemVert_Bottom = assembly.instances['Bottom'].vertices

vertex_DOF3 = assemVert_Bottom.findAt(
    ((0.0, -Thickness, 0.0),)
)
Displacement_Node_3 = assembly.Set(
    vertices = vertex_DOF3, 
    name = 'Displacement_Node-3'
)
mdb.models['Model-1'].DisplacementBC(
    name = 'Displacement_DOF-3', 
    createStepName = 'Initial', 
    region = Displacement_Node_3,
    u1 = SET, 
    u2 = SET, 
    u3 = SET, 
    ur1 = UNSET, 
    ur2 = UNSET, 
    ur3 = UNSET, 
    amplitude = UNSET, 
    distributionType = UNIFORM, 
    fieldName = '', 
    localCsys = None
)

vertex_DOF2 = assemVert_Bottom.findAt(
    ((0.0, -Thickness, Length),)
)
Displacement_Node_2 = assembly.Set(
    vertices = vertex_DOF2, 
    name = 'Displacement_Node-2'
)
mdb.models['Model-1'].DisplacementBC(
    name = 'Displacement_DOF-2', 
    createStepName = 'Initial', 
    region = Displacement_Node_2, 
    u1 = SET, 
    u2 = SET, 
    u3 = UNSET, 
    ur1 = UNSET, 
    ur2 = UNSET, 
    ur3 = UNSET, 
    amplitude = UNSET, 
    distributionType = UNIFORM, 
    fieldName = '', 
    localCsys = None
)

vertex_DOF1 = assemVert_Bottom.findAt(
    ((Width, -Thickness, 0.0),)
)
Displacement_Node_1 = assembly.Set(
    vertices = vertex_DOF1, 
    name = 'Displacement_Node-1'
)
mdb.models['Model-1'].DisplacementBC(
    name = 'Displacement_DOF-1', 
    createStepName = 'Initial', 
    region = Displacement_Node_1, 
    u1 = UNSET, 
    u2 = SET, 
    u3 = UNSET, 
    ur1 = UNSET, 
    ur2 = UNSET, 
    ur3 = UNSET, 
    amplitude = UNSET, 
    distributionType = UNIFORM, 
    fieldName = '', 
    localCsys = None
)

AbsTopFace = assembly.Set(
    name = 'AbsTopFace',
    faces = assembly.instances['Top'].faces.findAt(
        ((Width/2.0, Height+Thickness, Length/2.0),),
    )
)
mdb.models['Model-1'].DisplacementBC(
    name = 'Pre-Contact-Top', 
    createStepName = 'Pre-Contact', 
    region = AbsTopFace, 
    u1 = SET, 
    u2 = -0.0001, 
    u3 = SET, 
    ur1 = UNSET, 
    ur2 = UNSET, 
    ur3 = UNSET, 
    amplitude = UNSET, 
    distributionType = UNIFORM, 
    fieldName = '', 
    localCsys = None
)
mdb.models['Model-1'].boundaryConditions['Pre-Contact-Top'].deactivate('Loading')

Loading_Wall_X_Face = assembly.Set(
    name = 'Loading_Wall_X_Face',
    faces = assembly.instances['Wall_X'].faces.findAt(
        ((Width/2.0, Height/2.0, 0.0),),
        ((Thickness/2.0, Height/2.0, 0.0),),
        ((Width-(Thickness/2.0), Height/2.0, 0.0),)
    )
)
mdb.models['Model-1'].DisplacementBC(
    name = 'Pre-Contact-Wall_X', 
    createStepName = 'Pre-Contact', 
    region = Loading_Wall_X_Face, 
    u1 = SET, 
    u2 = SET, 
    u3 = 0.0001, 
    ur1 = UNSET, 
    ur2 = UNSET, 
    ur3 = UNSET, 
    amplitude = UNSET, 
    distributionType = UNIFORM, 
    fieldName = '', 
    localCsys = None
)
mdb.models['Model-1'].boundaryConditions['Pre-Contact-Wall_X'].deactivate('Loading')

Loading_Wall_XMir_Face = assembly.Set(
    name = 'Loading_Wall_XMir_Face',
    faces = assembly.instances['Wall_X-Mirrored'].faces.findAt(
        ((Width/2.0, Height/2.0, Length),),
        ((Thickness/2.0, Height/2.0, Length),),
        ((Width-(Thickness/2.0), Height/2.0, Length),)
    )
)
mdb.models['Model-1'].DisplacementBC(
    name = 'Pre-Contact-Wall_X-Mirrored', 
    createStepName = 'Pre-Contact', 
    region = Loading_Wall_XMir_Face, 
    u1 = SET, 
    u2 = SET, 
    u3 = -0.0001, 
    ur1 = UNSET, 
    ur2 = UNSET, 
    ur3 = UNSET, 
    amplitude = UNSET, 
    distributionType = UNIFORM, 
    fieldName = '', 
    localCsys = None
)
mdb.models['Model-1'].boundaryConditions['Pre-Contact-Wall_X-Mirrored'].deactivate('Loading')

Loading_Wall_Z_Face = assembly.Set(
    name = 'Loading_Wall_Z_Face',
    faces = assembly.instances['Wall_Z'].faces.findAt(
        ((0.0, Height/2.0, Length/2.0),),
        ((0.0, Height/2.0, Thickness/2.0),),
        ((0.0, Height/2.0, Length-(Thickness/2.0)),)
    )
)
mdb.models['Model-1'].DisplacementBC(
    name = 'Pre-Contact-Wall_Z', 
    createStepName = 'Pre-Contact', 
    region = Loading_Wall_Z_Face, 
    u1 = 0.0001, 
    u2 = SET, 
    u3 = SET, 
    ur1 = UNSET, 
    ur2 = UNSET, 
    ur3 = UNSET, 
    amplitude = UNSET, 
    distributionType = UNIFORM, 
    fieldName = '', 
    localCsys = None
)
mdb.models['Model-1'].boundaryConditions['Pre-Contact-Wall_Z'].deactivate('Loading')

Loading_Wall_ZMir_Face = assembly.Set(
    name = 'Loading_Wall_ZMir_Face',
    faces = assembly.instances['Wall_Z-Mirrored'].faces.findAt(
        ((Width, Height/2.0, Length/2.0),),
        ((Width, Height/2.0, Thickness/2.0),),
        ((Width, Height/2.0, Length-(Thickness/2.0)),)
    )
)
mdb.models['Model-1'].DisplacementBC(
    name = 'Pre-Contact-Wall_Z-Mirrored', 
    createStepName = 'Pre-Contact', 
    region = Loading_Wall_ZMir_Face, 
    u1 = -0.0001, 
    u2 = SET, 
    u3 = SET, 
    ur1 = UNSET, 
    ur2 = UNSET, 
    ur3 = UNSET, 
    amplitude = UNSET, 
    distributionType = UNIFORM, 
    fieldName = '', 
    localCsys = None
)
mdb.models['Model-1'].boundaryConditions['Pre-Contact-Wall_Z-Mirrored'].deactivate('Loading')

#------------------------------------------------------------------------
# Load Assignment
#------------------------------------------------------------------------
Loading_Bottom_Faces = assembly.Set(
    name = 'Loading_Bottom_Faces',
    faces = assembly.instances['Bottom'].faces.findAt(
        ((Width/2.0, -Thickness, Length/2.0),),
        ((0.0, -(Thickness/2.0), Length/2.0),), 
        ((Width/2.0, -(Thickness/2.0), 0.0),), 
        ((Width, -(Thickness/2.0), Length/2.0),), 
        ((Width/2.0, -(Thickness/2.0), Length),) 
    )
)
Loading_Top_Faces = assembly.Set(
    name = 'Loading_Top_Faces',
    faces = assembly.instances['Top'].faces.findAt(
        ((Width/2.0, Height+Thickness, Length/2.0),), 
        ((0.0, Height+(Thickness/2.0), Length/2.0),), 
        ((Width/2.0, Height+(Thickness/2.0), 0.0),), 
        ((Width, Height+(Thickness/2.0), Length/2.0),), 
        ((Width/2.0, Height+(Thickness/2.0), Length),)
    )
)
All_Faces = (
    Loading_Bottom_Faces.faces+
    Loading_Top_Faces.faces + 
    Loading_Wall_X_Face.faces + 
    Loading_Wall_Z_Face.faces + 
    Loading_Wall_XMir_Face.faces + 
    Loading_Wall_ZMir_Face.faces
)
LoadingSurface = assembly.Surface(
    side1Faces = All_Faces,
    name = 'Loading_Surface'
)
mdb.models['Model-1'].Pressure(
    name = 'Atmospheric_Pressure', 
    createStepName = 'Loading', 
    region = LoadingSurface, 
    distributionType = UNIFORM, 
    field = '', 
    magnitude = 0.101325, 
    amplitude = UNSET
)
