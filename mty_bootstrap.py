import os
import sys
import folder_paths

def bootstrap():
    framework_path = os.environ.get("MTY_FRAMEWORK_COMFY_PATH")

    if not framework_path:
        print("[MTY] No framework path found.")
        return

    print(f"[MTY] Framework path: {framework_path}")

    custom_nodes_path = os.path.join(
        framework_path,
        "custom_nodes"
    )

    if not os.path.exists(custom_nodes_path):
        print(f"[MTY] Custom nodes folder missing: {custom_nodes_path}")
        return

    custom_nodes_paths = folder_paths.folder_names_and_paths["custom_nodes"][0]

    if custom_nodes_path not in custom_nodes_paths:
        custom_nodes_paths.append(custom_nodes_path)

    print(f"[MTY] Registered custom nodes path: {custom_nodes_path}")