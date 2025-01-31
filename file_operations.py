from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs

def save_to_step(shape, filename):
    """
    Save the given shape to a STEP file.

    Parameters:
    shape (TopoDS_Shape): The shape to be saved.
    filename (str): The name of the STEP file to save the shape to.

    Returns:
    bool: True if the file was successfully written, False otherwise.
    """
    step_writer = STEPControl_Writer()
    step_writer.Transfer(shape, STEPControl_AsIs)
    status = step_writer.Write(filename)
    return status == 1