python scripts/export_litert_baseline_task3.py 
./firmware/build_firmware.sh
python host/run_submission.py   --task 3   --split validation   --source clean   --port /dev/ttyACM0   --uf2 firmware/build/vlp_pico.uf2