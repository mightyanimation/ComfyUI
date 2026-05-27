import os
import logging
import folder_paths

logger = logging.getLogger("mty_bootstrap")

def bootstrap():
    logger.info("[MTY] === BOOTSTRAP START ===")

    framework_path = os.environ.get("MTY_FRAMEWORK_COMFY_PATH")

    logger.info(f"[MTY] Framework env path: {framework_path}")

    if not framework_path:
        logger.warning("[MTY] No framework path found.")
        return

    custom_nodes_path = os.path.join(
        framework_path,
        "custom_nodes"
    )

    logger.info(f"[MTY] Custom nodes path: {custom_nodes_path}")

    if not os.path.exists(custom_nodes_path):
        logger.warning("[MTY] Custom nodes folder does not exist.")
        return

    custom_nodes_paths = folder_paths.folder_names_and_paths["custom_nodes"][0]

    logger.info(f"[MTY] Existing custom_nodes paths: {custom_nodes_paths}")

    if custom_nodes_path not in custom_nodes_paths:
        custom_nodes_paths.append(custom_nodes_path)
        logger.info("[MTY] Custom nodes path appended.")
    else:
        logger.info("[MTY] Custom nodes path already registered.")

    logger.info(f"[MTY] Final custom_nodes paths: {custom_nodes_paths}")

    logger.info("[MTY] === BOOTSTRAP END ===")