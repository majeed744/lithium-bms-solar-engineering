CELL_SPECS = {
    "1": {"name": "LiFePO4 (LFP)", "nom_v": 3.20, "max_v": 3.65, "min_v": 2.50},
    "2": {"name": "Li-ion (NMC/NCA)", "nom_v": 3.70, "max_v": 4.20, "min_v": 3.00}
}

def calculate_pack(chem_key, series_count, parallel_count, cell_ah, cell_weight_kg):
    chem = CELL_SPECS[chem_key]
    total_cells = series_count * parallel_count
    pack_ah = parallel_count * cell_ah
    nom_voltage = series_count * chem["nom_v"]
    max_voltage = series_count * chem["max_v"]
    cutoff_voltage = series_count * chem["min_v"]
    total_kwh = (nom_voltage * pack_ah) / 1000.0
    usable_kwh = total_kwh * 0.80
    safe_charge_amps = pack_ah * 0.5
    max_discharge_amps = pack_ah * 1.0
    max_inverter_kw = (nom_voltage * max_discharge_amps) / 1000.0
    est_pack_weight = total_cells * cell_weight_kg * 1.15

    print("\n" + "=" * 50)
    print(f"LITHIUM PACK SPECIFICATION REPORT ({series_count}S{parallel_count}P)")
    print("=" * 50)
    print(f"Chemistry:              {chem['name']}")
    print(f"Total Cells Required:   {total_cells} cells ({cell_ah} Ah each)")
    print(f"Total Pack Capacity:    {pack_ah:.1f} Ah | {total_kwh:.2f} kWh")
    print(f"Usable Energy (80% DoD):{usable_kwh:.2f} kWh")
    print(f"Estimated Pack Weight:  {est_pack_weight:.1f} kg (incl. casing & BMS)")
    print("-" * 50)
    print(f"Nominal Pack Voltage:   {nom_voltage:.2f} V")
    print(f"BMS Full Charge Cutoff: {max_voltage:.2f} V ({chem['max_v']}V/cell)")
    print(f"BMS Low-Voltage Cutoff: {cutoff_voltage:.2f} V ({chem['min_v']}V/cell)")
    print("-" * 50)
    print(f"Recommended Charge (0.5C):    {safe_charge_amps:.1f} A")
    print(f"Max Continuous Discharge (1C):{max_discharge_amps:.1f} A")
    print(f"Max Recommended Inverter:     {max_inverter_kw:.2f} kW")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    print("=== LITHIUM BATTERY PACK CONFIGURATOR ===")
    print("Select Cell Chemistry:\n  1. LiFePO4 (3.2V nominal)\n  2. Li-ion NMC/NCA (3.7V nominal)")
    choice = input("Enter 1 or 2: ").strip()
    if choice not in CELL_SPECS:
        print("Invalid chemistry choice. Please run again and enter 1 or 2.")
    else:
        s = int(input("Enter number of cells in SERIES (e.g., 8 for 8S): "))
        p = int(input("Enter number of cells in PARALLEL (e.g., 4 for 4P): "))
        ah = float(input("Enter single cell capacity in Ah (e.g., 63.3): "))
        wt = float(input("Enter single cell weight in kg (e.g., 1.15): "))
        calculate_pack(choice, s, p, ah, wt)
