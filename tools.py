import os
import importlib
import inspect
from langchain.tools.base import BaseTool
from typing import List

def load_langchain_tools_from_folder(
    folder_path: str,
    module_names: List[str] = None  # Optional list of module names (without .py)
) -> List[BaseTool]:
    """
    Dynamically load all LangChain @tool-decorated tools from the specified folder.

    Args:
        folder_path (str): Path to the folder containing .py files with tools.
        module_names (List[str], optional): Specific module names to include.
                                            If None, all .py files in the folder are scanned.

    Returns:
        List[BaseTool]: List of collected LangChain tool instances.
    """
    tools = []

    for file in os.listdir(folder_path):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = file[:-3]  # Strip .py
            if module_names and module_name not in module_names:
                continue

            # Construct full import path
            relative_module = os.path.relpath(folder_path).replace(os.path.sep, ".")
            full_module_path = f"{relative_module}.{module_name}".strip(".")

            try:
                mod = importlib.import_module(full_module_path)
                # Collect all BaseTool instances
                module_tools = [
                    obj for _, obj in inspect.getmembers(mod)
                    if isinstance(obj, BaseTool)
                ]
                tools.extend(module_tools)
            except Exception as e:
                print(f"Failed to load module {module_name}: {e}")

    return tools


from myapp.tools_loader import load_langchain_tools_from_folder

tools = load_langchain_tools_from_folder(
    folder_path="myapp/tools",                # Relative path to folder
    module_names=["candidate_tools", "job_tools"]  # Optional: only load these
)
