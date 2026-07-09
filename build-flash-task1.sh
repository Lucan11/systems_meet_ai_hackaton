python scripts/export_litert_baseline.py 
./firmware/build_firmware.sh
python host/run_submission.py   --task 1   --split validation   --source clean   --port /dev/ttyACM0   --uf2 firmware/build/vlp_pico.uf2