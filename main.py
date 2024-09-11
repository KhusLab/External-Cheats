import ctypes
import utility
from ctypes import wintypes
from constants import *

kernel32 = ctypes.windll.kernel32

pid = utility.GetProcId("client exe file")
handle = kernel32.OpenProcess(PROCESS_ALL_ACCESS, 0, ctypes.wintypes.DWORD(pid))
base_address = utility.GetModuleBaseAddress(pid, "client exe file")

ammo_decrement = base_address + 0xC73EF
utility.nopBytes(handle, ammo_decrement, 2)

current_ammo_base = base_address +0x0016F338
current_ammo_address = utility.FindMyDMAAddy(handle, current_ammo_address, [0x0, 0xB8, 0x140], 32)
kernel32.WriteProcessMemory(handle, current_ammo_address, ctypes.byref(ctypes.c_int(1337)), ctypes.sizeof(ctypes.c_int), None)
kernel32.CloseHandle(handle)