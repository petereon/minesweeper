from battleship.logic.constants import (
    Vessel,
    VesselIdentifier,
    column_mapping,
    row_mapping,
)
from battleship.logic.grid import Grid


class Player:
    def __init__(self):
        self.ocean_grid = Grid()
        self.target_grid = Grid()

    def get_ship_coordinates(self, coordinates: tuple) -> tuple:
        start_column_idx = column_mapping[coordinates[0][0]]
        start_row_idx = row_mapping[coordinates[0][1]]
        end_column_idx = column_mapping[coordinates[1][0]]
        end_row_idx = row_mapping[coordinates[1][1]]
        return ((start_column_idx, start_row_idx), (end_column_idx, end_row_idx))

    def place_vessel(self, vessel_type: Vessel, coordinates: tuple):
        ((start_column_idx, start_row_idx), (end_column_idx, end_row_idx)) = self.get_ship_coordinates(coordinates)
        self.ocean_grid.matrix[start_column_idx][start_row_idx] = VesselIdentifier[vessel_type.value]
        if start_column_idx != end_column_idx:
            current_column_idx = start_column_idx
            while current_column_idx < end_column_idx:
                current_column_idx += 1
                self.ocean_grid.matrix[current_column_idx][start_row_idx] = VesselIdentifier[vessel_type.value]
        else:
            self.ocean_grid.matrix[start_column_idx][start_row_idx + 1] = VesselIdentifier[vessel_type.value]
            self.ocean_grid.matrix[start_column_idx][start_row_idx + 2] = VesselIdentifier[vessel_type.value]
            self.ocean_grid.matrix[start_column_idx][start_row_idx + 3] = VesselIdentifier[vessel_type.value]
            self.ocean_grid.matrix[end_column_idx][end_row_idx] = VesselIdentifier[vessel_type.value]
