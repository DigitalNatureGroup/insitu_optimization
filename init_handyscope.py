import libtiepie
from printinfo import *
## Init HandyScope
# Print library info:
print_library_info()

# Enable network search:
libtiepie.network.auto_detect_enabled = True

# Search for devices:
libtiepie.device_list.update()

# Try to open an oscilloscope with block measurement support:
scp = None
for item in libtiepie.device_list:
    if item.can_open(libtiepie.DEVICETYPE_OSCILLOSCOPE):
        scp = item.open_oscilloscope()
        if scp.measure_modes & libtiepie.MM_BLOCK:
            break
        else:
            scp = None

scp.measure_mode = libtiepie.MM_BLOCK
# Set sample frequency:
scp.sample_frequency = 1e6  # 1 MHz
# Set record length:
scp.record_length = 50000  # 10000 samples
# Set pre sample ratio:
scp.pre_sample_ratio = 0  # 0 %
# For all channels:
for ch in scp.channels:
        # Enable channel to measure it:
    ch.enabled = True
    # Set range:
    ch.range = 4  
    # Set coupling:
    ch.coupling = libtiepie.CK_DCV  # DC Volt
# Set trigger timeout:
scp.trigger_time_out = 100e-3  # 100 ms
# Disable all channel trigger sources:
for ch in scp.channels:
    ch.trigger.enabled = False
# Setup channel trigger:
ch = scp.channels[0]  # Ch 1
# Enable trigger source:
ch.trigger.enabled = True
# Kind:
ch.trigger.kind = libtiepie.TK_RISINGEDGE  # Rising edge
# Level:
ch.trigger.levels[0] = 0.5  # 50 %
# Hysteresis:
ch.trigger.hystereses[0] = 0.05  # 5 %
# Print oscilloscope info:
print_device_info(scp)