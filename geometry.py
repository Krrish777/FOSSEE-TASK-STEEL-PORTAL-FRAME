from OCC.Core.gp import gp_Vec, gp_Trsf, gp_Ax1, gp_Pnt, gp_Dir
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
import math

# Create an I-section solid
def create_i_section(length, width, depth, flange_thickness, web_thickness):
    web_height = depth - 2 * flange_thickness
    bottom_flange = BRepPrimAPI_MakeBox(length, width, flange_thickness).Shape()
    top_flange = BRepPrimAPI_MakeBox(length, width, flange_thickness).Shape()
    trsf = gp_Trsf()
    trsf.SetTranslation(gp_Vec(0, 0, depth - flange_thickness))
    top_flange_transform = BRepBuilderAPI_Transform(top_flange, trsf, True).Shape()

    web = BRepPrimAPI_MakeBox(length, web_thickness, web_height).Shape()
    trsf.SetTranslation(gp_Vec(0, (width - web_thickness) / 2, flange_thickness))
    web_transform = BRepBuilderAPI_Transform(web, trsf, True).Shape()

    i_section_solid = BRepAlgoAPI_Fuse(bottom_flange, top_flange_transform).Shape()
    i_section_solid = BRepAlgoAPI_Fuse(i_section_solid, web_transform).Shape()

    return i_section_solid

# Create a layout of purlins
def create_purlin_layout(num_purlins, purlin_width, purlin_height, purlin_depth, rafter_angle, column_height):
    purlin = BRepPrimAPI_MakeBox(purlin_width, purlin_depth, purlin_height).Shape()
    roof_rise = (8400 / 2) * math.tan(math.radians(rafter_angle))
    purlins = None
    
    for i in range(num_purlins):
        x = i * (8000 - purlin_width) / (num_purlins - 1)
        z = column_height + roof_rise - (i - num_purlins / 2) * (roof_rise / (num_purlins / 2)) if i >= num_purlins / 2 else column_height + roof_rise - (num_purlins / 2 - i) * (roof_rise / (num_purlins / 2))

        trsf = gp_Trsf()
        trsf.SetTranslation(gp_Vec(x, 0, z))
        purlin_instance = BRepBuilderAPI_Transform(purlin, trsf, True).Shape()

        if purlins is None:
            purlins = purlin_instance
        else:
            purlins = BRepAlgoAPI_Fuse(purlins, purlin_instance).Shape()
    
    return purlins

# Create a portal frame
def create_portal_frame(column, num_columns_per_side, num_purlins, purlin_width, purlin_height, purlin_depth, 
                        rafter_width, rafter_depth, rafter_flange_thickness, rafter_web_thickness, rafter_angle, 
                        num_rafters, column_height):
    columns = None
    column_spacing = purlin_depth / (num_columns_per_side - 1)
    
    rafter_length = 8000 / 2 / math.cos(math.radians(rafter_angle))
    rafter = create_i_section(rafter_length, rafter_width, rafter_depth, rafter_flange_thickness, rafter_web_thickness)
    
    for i in range(num_columns_per_side):
        y = i * column_spacing
        x_left = -8000 / 2 + 4000
        trsf_left = gp_Trsf()
        trsf_left.SetTranslation(gp_Vec(x_left, y, 0))
        column_instance_left = BRepBuilderAPI_Transform(column, trsf_left, True).Shape()

        x_right = 8000 / 2 + 4000
        trsf_right = gp_Trsf()
        trsf_right.SetTranslation(gp_Vec(x_right, y, 0))
        column_instance_right = BRepBuilderAPI_Transform(column, trsf_right, True).Shape()

        if columns is None:
            columns = BRepAlgoAPI_Fuse(column_instance_left, column_instance_right).Shape()
        else:
            columns = BRepAlgoAPI_Fuse(columns, column_instance_left).Shape()
            columns = BRepAlgoAPI_Fuse(columns, column_instance_right).Shape()

    purlins = create_purlin_layout(num_purlins, purlin_width, purlin_height, purlin_depth, rafter_angle, column_height)

    rafters = None
    rafter_spacing = purlin_depth / (num_rafters - 1)

    for i in range(num_rafters):
        y = i * rafter_spacing
        trsf_left = gp_Trsf()
        trsf_left.SetTranslation(gp_Vec(-8000 / 2 + 4000, y, column_height))
        rafter_instance_left = BRepBuilderAPI_Transform(rafter, trsf_left, True).Shape()

        rotation_left = gp_Trsf()
        rotation_left.SetRotation(gp_Ax1(gp_Pnt(-8000 / 2 + 4000, y, column_height), gp_Dir(0, -1, 0)), math.radians(rafter_angle))
        rafter_instance_left = BRepBuilderAPI_Transform(rafter_instance_left, rotation_left, True).Shape()

        trsf_right = gp_Trsf()
        trsf_right.SetTranslation(gp_Vec(8000 / 2 + 4000 - 4000, y, column_height))
        rafter_instance_right = BRepBuilderAPI_Transform(rafter, trsf_right, True).Shape()

        rotation_right = gp_Trsf()
        rotation_right.SetRotation(gp_Ax1(gp_Pnt(8000 / 2 + 4000 - 4000, y, column_height), gp_Dir(0, -1, 0)), math.radians(-rafter_angle))
        rafter_instance_right = BRepBuilderAPI_Transform(rafter_instance_right, rotation_right, True).Shape()

        alignment_shift = gp_Trsf()
        alignment_shift.SetTranslation(gp_Vec(0, 0, (8000 / 2) * math.tan(math.radians(rafter_angle))))
        rafter_instance_right = BRepBuilderAPI_Transform(rafter_instance_right, alignment_shift, True).Shape()

        if rafters is None:
            rafters = BRepAlgoAPI_Fuse(rafter_instance_left, rafter_instance_right).Shape()
        else:
            rafters = BRepAlgoAPI_Fuse(rafters, rafter_instance_left).Shape()
            rafters = BRepAlgoAPI_Fuse(rafters, rafter_instance_right).Shape()

    portal_frame_solid = BRepAlgoAPI_Fuse(columns, purlins).Shape()
    portal_frame_solid = BRepAlgoAPI_Fuse(portal_frame_solid, rafters).Shape()

    return portal_frame_solid