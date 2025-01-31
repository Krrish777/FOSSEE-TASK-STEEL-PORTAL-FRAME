from PySide6.QtWidgets import QWidget, QLineEdit, QGridLayout, QLabel, QVBoxLayout, QSizePolicy

class Widget(QWidget):
    """
    A QWidget subclass that creates a GUI for Steel Frame Design.
    This widget contains multiple QLineEdit fields for inputting various parameters
    related to the design of a steel frame.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Steel Frame Design")

        # Main layout for the widget
        layout = QVBoxLayout()
        grid_layout = QGridLayout()

        # Create the QLineEdit fields for various parameters
        self.column_height = QLineEdit()
        self.column_length = QLineEdit()
        self.column_width = QLineEdit()
        self.column_flange_thickness = QLineEdit()
        self.column_web_thickness = QLineEdit()
        self.num_columns_per_side = QLineEdit()
        self.num_rafters = QLineEdit()
        self.rafter_width = QLineEdit()
        self.rafter_depth = QLineEdit()
        self.rafter_flange_thickness = QLineEdit()
        self.rafter_web_thickness = QLineEdit()
        self.rafter_angle = QLineEdit()
        self.num_purlins = QLineEdit()
        self.purlin_width = QLineEdit()
        self.purlin_height = QLineEdit()
        self.purlin_depth = QLineEdit()

        # Set size policy for each QLineEdit to allow it to expand
        for field in [
            self.column_height, self.column_length, self.column_width,
            self.column_flange_thickness, self.column_web_thickness,
            self.num_columns_per_side, self.num_rafters, self.rafter_width,
            self.rafter_depth, self.rafter_flange_thickness, self.rafter_web_thickness,
            self.rafter_angle, self.num_purlins, self.purlin_width, self.purlin_height,
            self.purlin_depth
        ]:
            field.setMinimumWidth(150)
            field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # Add labels and QLineEdits to the grid layout
        grid_layout.addWidget(QLabel("Column Height"), 0, 0)
        grid_layout.addWidget(self.column_height, 0, 1)
        grid_layout.addWidget(QLabel("Column Length"), 1, 0)
        grid_layout.addWidget(self.column_length, 1, 1)
        grid_layout.addWidget(QLabel("Column Width"), 2, 0)
        grid_layout.addWidget(self.column_width, 2, 1)
        grid_layout.addWidget(QLabel("Column Flange Thickness"), 3, 0)
        grid_layout.addWidget(self.column_flange_thickness, 3, 1)
        grid_layout.addWidget(QLabel("Column Web Thickness"), 4, 0)
        grid_layout.addWidget(self.column_web_thickness, 4, 1)
        grid_layout.addWidget(QLabel("Number of Columns Per Side"), 5, 0)
        grid_layout.addWidget(self.num_columns_per_side, 5, 1)
        grid_layout.addWidget(QLabel("Number of Rafters"), 6, 0)
        grid_layout.addWidget(self.num_rafters, 6, 1)
        grid_layout.addWidget(QLabel("Rafter Width"), 7, 0)
        grid_layout.addWidget(self.rafter_width, 7, 1)
        grid_layout.addWidget(QLabel("Rafter Depth"), 8, 0)
        grid_layout.addWidget(self.rafter_depth, 8, 1)
        grid_layout.addWidget(QLabel("Rafter Flange Thickness"), 9, 0)
        grid_layout.addWidget(self.rafter_flange_thickness, 9, 1)
        grid_layout.addWidget(QLabel("Rafter Web Thickness"), 10, 0)
        grid_layout.addWidget(self.rafter_web_thickness, 10, 1)
        grid_layout.addWidget(QLabel("Rafter Angle"), 11, 0)
        grid_layout.addWidget(self.rafter_angle, 11, 1)
        grid_layout.addWidget(QLabel("Number of Purlins"), 12, 0)
        grid_layout.addWidget(self.num_purlins, 12, 1)
        grid_layout.addWidget(QLabel("Purlin Width"), 13, 0)
        grid_layout.addWidget(self.purlin_width, 13, 1)
        grid_layout.addWidget(QLabel("Purlin Height"), 14, 0)
        grid_layout.addWidget(self.purlin_height, 14, 1)
        grid_layout.addWidget(QLabel("Purlin Depth"), 15, 0)
        grid_layout.addWidget(self.purlin_depth, 15, 1)

        # Set the column stretch for the grid layout
        grid_layout.setColumnStretch(0, 0)
        grid_layout.setColumnStretch(1, 1)
        layout.addLayout(grid_layout)
        
        self.setLayout(layout)
