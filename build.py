import PyInstaller.__main__

PyInstaller.__main__.run([
    '--onefile',  
    '--add-data', 'assets;assets',  
    'labirint_finish.py', 
])


#simpan file python ini di folder yang sama dengan file python untuk program game nya
#semua file gambar dan dile2 pendukung untuk game di simpan di subfolder assets tetap di dalam folder yang sama ddengan file python ini dan file python game