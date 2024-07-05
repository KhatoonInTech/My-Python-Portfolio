import cx_Freeze
import os
import sys

PYTHON_INSTALL_DIR= os.path.dirname(sys.executable)
os.environ['TCL_LIBRARY']= os.path.join(PYTHON_INSTALL_DIR,'tcl','tcl8.6')
os.environ['TK_LIBRARY']= os.path.join(PYTHON_INSTALL_DIR,'tk','tk8.6')

include_files=[
    (
        os.path.join( PYTHON_INSTALL_DIR,'DLLs','tk86t.dll'),
        os.path.join('lib','tk86.dll')
   ),
   (    
       os.path.join(PYTHON_INSTALL_DIR,'DLLs','tcl86t.dll'),
       os.path.join(PYTHON_INSTALL_DIR,'DLLs','tcl86.dll')
       
   )
   ]
#name
name="InvenTria"

#option
option={
    "build_exe":{
        'include_files': include_files
    }
}

#base
base=None
if sys.platform=='win32':
    base='Win32GUI'

executables=[
    cx_Freeze.Executable("app.py",
                          icon=r'C:\Users\Super\Desktop\InvenTria\exe-file.png',
                         shortcut_name="InvenTria",
                         shortcut_dir="DesktopFolder",
                         base=base
                         )]

#setup function
cx_Freeze.setup(
    name=name,
    version="1.0",
    author="Ayesha Noreen",
    description="Best Inventory Manager in your hands",
    option=option,
    executables=executables
)