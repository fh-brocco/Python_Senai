import speedTest  
test = speedTest.Speedtest()
down = test.download()
up = test.upload()
print(f'Taxa de Download: {down:.2f}')
print(f'Taxa de Upload: {up:.2f}')