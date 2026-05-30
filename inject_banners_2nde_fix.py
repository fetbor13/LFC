import re
import os

files_and_sims = {
    "2nde_chapitre2.html": "sound_waves",
    "2nde_chapitre4.html": "refraction",
    "2nde_chapitre5.html": "spectra",
    "2nde_chapitre6.html": "atom_builder",
    "2nde_chapitre11.html": "chemical_conservation",
    "2nde_chapitre14.html": "inertia",
    "2nde_chapitre16.html": "states_of_matter"
}

banner_template = """
<div style="background: linear-gradient(135deg, #172033, #0f172a); border-radius: 16px; padding: 24px; color: white; display: flex; align-items: center; justify-content: space-between; margin-bottom: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.2); border: 1px solid rgba(255,255,255,0.1); margin-top: 20px;">
  <div>
    <h4 style="margin: 0 0 8px 0; font-size: 20px; font-weight: 800; display: flex; align-items: center; gap: 10px;">
      <span style="font-size: 24px;">🧪</span> NEXUS : Laboratoire Virtuel
    </h4>
    <p style="margin: 0; color: #94a3b8; font-size: 15px; max-width: 500px;">
      Accédez à la simulation interactive complète et haute précision de ce chapitre dans le nouveau hub WebOS.
    </p>
  </div>
  <a href="index_sim.html?sim={sim_id}" style="background: linear-gradient(135deg, #2ca66f, #208b5a); color: white; text-decoration: none; padding: 12px 24px; border-radius: 8px; font-weight: 700; display: inline-block; transition: transform 0.2s, box-shadow 0.2s; box-shadow: 0 4px 14px rgba(44,166,111,0.3);">
    Lancer la Simulation →
  </a>
</div>
"""

for filename, sim_id in files_and_sims.items():
    if not os.path.exists(filename):
        continue

    with open(filename, 'r') as f:
        content = f.read()

    if "NEXUS : Laboratoire Virtuel" in content:
        print(f"Skipping {filename}, already injected.")
        continue

    banner = banner_template.format(sim_id=sim_id)

    # regex for id="p-simulations"
    pattern = r'(id="p-simulations"[^>]*>|id="p-sim"[^>]*>)'
    match = re.search(pattern, content)

    if match:
        insertion_point = match.end()
        new_content = content[:insertion_point] + banner + content[insertion_point:]
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"Injected into {filename} with sim={sim_id}")
    else:
        print(f"Could not find injection point in {filename}")
