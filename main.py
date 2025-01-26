from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from geometry import create_i_section, create_portal_frame
from file_operations import save_to_step
from OCC.Display.SimpleGui import init_display
from gui import Widget
import sys

class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Steel Frame Design Application")
        self.setGeometry(100, 100, 800, 600)
        
        # Main layout
        main_layout = QVBoxLayout()

        self.input_widget = Widget()
        main_layout.addWidget(self.input_widget)
        
        self.generate_button = QPushButton("Generate and Display Frame")
        self.generate_button.clicked.connect(self.generate_frame)
        main_layout.addWidget(self.generate_button)
        
        self.setLayout(main_layout)

    def generate_frame(self):
        try:
            # Read values from the GUI
            column_height = float(self.input_widget.column_height.text())
            column_length = float(self.input_widget.column_length.text())
            column_width = float(self.input_widget.column_width.text())
            column_flange_thickness = float(self.input_widget.column_flange_thickness.text())
            column_web_thickness = float(self.input_widget.column_web_thickness.text())
            num_columns_per_side = int(self.input_widget.num_columns_per_side.text())
            num_rafters = int(self.input_widget.num_rafters.text())
            rafter_width = float(self.input_widget.rafter_width.text())
            rafter_depth = float(self.input_widget.rafter_depth.text())
            rafter_flange_thickness = float(self.input_widget.rafter_flange_thickness.text())
            rafter_web_thickness = float(self.input_widget.rafter_web_thickness.text())
            rafter_angle = float(self.input_widget.rafter_angle.text())
            num_purlins = int(self.input_widget.num_purlins.text())
            purlin_width = float(self.input_widget.purlin_width.text())
            purlin_height = float(self.input_widget.purlin_height.text())
            purlin_depth = float(self.input_widget.purlin_depth.text())

            # Create the steel frame
            column = create_i_section(column_length, column_width, column_height, 
                                       column_flange_thickness, column_web_thickness)
            
            portal_frame = create_portal_frame(
                column, num_columns_per_side, num_purlins, purlin_width, purlin_height, 
                purlin_depth, rafter_width, rafter_depth, rafter_flange_thickness, 
                rafter_web_thickness, rafter_angle, num_rafters, column_height
            )
            
            # Display the frame
            display, start_display, add_menu, add_function_to_menu = init_display()
            display.DisplayShape(portal_frame, update=True)
            display.FitAll()

            # Save the frame to a STEP file
            filename = "portal_frame.stp"
            if save_to_step(portal_frame, filename):
                print(f"Successfully saved the portal frame to {filename}")
            else:
                print(f"Failed to save the portal frame to {filename}")
            
            start_display()

        except ValueError as e:
            print(f"Invalid input: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec())