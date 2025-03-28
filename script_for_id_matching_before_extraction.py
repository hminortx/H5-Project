# Full list of provided IDs (you can use the same list you provided earlier)
provided_ids = [
    "GU052149.1", "GU052104.1", "GU052096.1", "HM114454.1", "HM114470.1", "HM114446.1", "HM114462.1",
    "CY111595.1", "EF456776.1", "EF467807.1", "HM114478.1", "HM114502.1", "HM114494.1", "HM114493.1",
    "HM114510.1", "HM114518.1", "AB598126.1", "HM172438.1", "HM172413.1", "HM172451.1", "EU146671.1",
    "CY116643.1", "JX235396.1", "EU146631.1", "EU146679.1", "EU146634.1", "HM114526.1", "HQ200462.1",
    "HQ664943.1", "HM114534.1", "CY014175.1", "CY014320.1", "EU146647.1", "EU146655.1", "CY014325.1",
    "EU146663.1", "CY014333.1", "EU146843.1", "CY017683.1", "EU146844.1", "EU146720.1", "EU146846.1",
    "CY014346.1", "CY014341.1", "CY014348.1", "EU146712.1", "CY014337.1", "EU146704.1", "CY014352.1",
    "EU146728.1", "CY014359.1", "CY014356.1", "CY014367.1", "EU146736.1", "CY014375.1", "CY098631.1",
    "CY098638.1", "CY014308.1", "CY014383.1", "EU146775.1", "CY014269.1", "CY014285.1", "EU146784.1",
    "CY098645.1", "CY014392.1", "CY014391.1", "EU146776.1", "CY014404.1", "CY014420.1", "EU146744.1",
    "EU146752.1", "CY014277.1", "EU146774.1", "CY014293.1", "CY014396.1", "CY014476.1", "EU146800.1",
    "CY014412.1", "CY014428.1", "EU146792.1", "CY014452.1", "CY014436.1", "CY014468.1", "EU146747.1",
    "CY014444.1", "CY014460.1", "CY098652.1", "CY014492.1", "CY014512.1", "CY014520.1", "EU146816.1",
    "EU146808.1", "CY014484.1", "EU146824.1", "CY014500.1", "CY014526.2", "CY014534.1", "GQ466181.3",
    "CY017659.1", "CY017667.1", "CY017675.1", "CY017685.1", "CY017643.1", "CY017635.1", "CY017651.1",
    "CY098665.1", "HM114550.1", "CY019349.1", "CY019357.1", "CY019381.1", "CY019389.1", "CY019413.1",
    "CY019429.1", "CY019373.1", "CY019365.1", "CY019397.1", "CY019405.1", "CY019421.1", "CY098678.1",
    "HQ200569.1", "HM114542.1", "HM114558.1", "HM114566.1", "HM114574.1", "HM114582.1", "HM114590.1",
    "CY098685.1", "HM114598.1", "CY098692.1", "FJ573465.1", "CY098699.1", "HM114614.1", "HM114606.1",
    "CY098713.1", "CY098720.1", "CY098727.1", "CY098741.1", "CY098734.1", "CY098748.1", "CY098755.1",
    "HQ652630.1", "JN588925.1", "JN588926.1", "CY088766.1", "JN588927.1", "JN588928.1", "JQ714243.1",
    "KF369203.1", "KF369211.1", "KF001369.1", "KF001377.1", "KF001385.1", "KF001393.1", "KF001401.1",
    "KF001409.1", "KF918495.1", "KF918453.1", "KF918461.1", "KF918487.1", "KF918503.1", "KF918511.1",
    "KF918527.1", "KP702162.1", "KP702170.1", "KX247639.1"
]

# Read IDs from a file (replace 'your_file.txt' with the actual path to your file)
def read_ids_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read and clean the lines to get a list of IDs
        file_ids = [line.strip() for line in file.readlines()]
    return set(file_ids)

# Path to your file containing extracted Newick IDs
file_path = r"C:\Users\hmino\OneDrive\Desktop\1998_filtered_sequences.txt"  # Replace with the actual path to your file

# Read IDs from the file
file_ids = read_ids_from_file(file_path)

# Find missing IDs
missing_ids = [id for id in provided_ids if id not in file_ids]

# Output missing IDs
if missing_ids:
    print("Missing IDs:", missing_ids)
else:
    print("No IDs are missing!")

# Add missing IDs to the file IDs (if needed)
file_ids.update(missing_ids)

# If you want to save the updated IDs to a new file
with open('updated_ids.txt', 'w') as updated_file:
    updated_file.write("\n".join(file_ids))

# Print the number of sequences in the new file
print(f"Total sequences in the new file: {len(file_ids)}")

