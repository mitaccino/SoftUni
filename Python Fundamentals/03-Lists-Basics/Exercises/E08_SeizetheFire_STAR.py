all_cells = input().split("#")
water = int(input())
total_efforts = 0
total_fire = 0
cells_value = []
for cell in all_cells:
    curr_cell = cell.split(" = ")
    type_fire = curr_cell[0]
    cell_value = int(curr_cell[-1])
    if type_fire == "High":
        if not 81 <= cell_value <= 125:
            continue
    elif type_fire == "Medium":
        if not 51 <= cell_value <= 80:
            continue
    elif type_fire == "Low":
        if not 1 <= cell_value <= 50:
            continue
    if water < cell_value:
        continue
    cells_value.append(cell_value)
    water -= cell_value
    total_efforts += cell_value * 0.25
    total_fire += cell_value
print("Cells:")
for cell in cells_value:
    print(f" - {cell}")
print(f"Effort: {total_efforts:.2f}")
print(f"Total Fire: {total_fire}")


