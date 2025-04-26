list_vokal = ["A", "I", "U", "E", "O"]
nama_lengkap = "FredrikATamunete"
huruf_konsonan = 0

for huruf in nama_lengkap:
      if not any(huruf.upper() == h for h in list_vokal):
        huruf_konsonan += 1
        

print("jumlah huruf konsonan pada {nama_lengkap} adalah {huruf_konsonan}")