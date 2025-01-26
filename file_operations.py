from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
def save_to_step(shape, filename):
    step_writer = STEPControl_Writer()
    step_writer.Transfer(shape, STEPControl_AsIs)
    status = step_writer.Write(filename)
    return status == 1