# import pytube https://github.com/pytube/pytube

from pytube import YouTube
import os


chan = ["/", "\", "(", ")", "&", "%", "-", "-", "*", " ", "$", "!"]

def main():
    vids = []
    fflist = []
    print("not: indirilen videolar .py ile aynı klasöre gelicektir")
    print("Video link: ")
    link = input()
    yt = YouTube(link)
    i = 0
    # 1080p ses olmadan
    x = yt.streams.filter(resolution="1080p", file_extension="mp4", only_video=True, progressive=False)
    # 720p ses + video
    y = yt.streams.filter(resolution="720p", file_extension="mp4", progressive=True)
    # 480p ses + video
    z = yt.streams.filter(resolution="480p", file_extension="mp4", progressive=True)
    print("")
    print("Bulunan Video + Ses kaynaklar [1080p ses içermez.]")
    print("")
    print("kalite" + "\t" + "fps" + "\t" + "format" + "\t" + "\t" + "type" + "\t" + "acodec" + "\t" + "itag")
    for data in x:
        print(str(i)+"- " + "1080p" + "\t" + str(data.fps) + "\t" + data.mime_type + "\t" + data.type + "\t" + "None" + "\t" + str(data.itag))   
        vids.append(data)
        i += 1
    for data in y:
        print(str(i)+"- " + "720p" + "\t" + str(data.fps) + "\t" + data.mime_type + "\t" + data.type + "\t" + data.abr + "\t" + str(data.itag)) 
        vids.append(data)
        i += 1
    for data in z:
        print(str(i)+"- " + "480p" + "\t" + str(data.fps) + "\t" + data.mime_type + "\t" + data.type + "\t" + data.abr + "\t" + str(data.itag))
        vids.append(data)
        i += 1
    # sadece ses
    print("")
    print("Sadece ses bulunan kaynaklar;")
    print("")
    c = yt.streams.filter(only_audio= True, progressive= False)
    for data in c:
        vids.append(data)
        print(str(i)+"- " + "None" + "\t" + "None" + " \t" + data.mime_type + "\t" + data.type + "\t" + data.abr + "\t" + str(data.itag))
        i += 1
    print("")
    print("indirilecekleri seçin (boşluksuz, virgül olmadan):")
    print("0 ve 4 indirmek için = '04' yazın")
    xc = input()
    xc.replace(" ", "")
    xf = list(xc)
    cwd = os.getcwd()
    for data in xf:
        print(f"indiriliyor.. {data}")
        try:
            ax = vids[int(data)].download()
            base, ext = os.path.splitext(ax)
            new_name = base + str(data) + ext
            for d in chan:
                new_name = new_name.replace(d, "")
            os.rename(ax, new_name)
            fflist.append(new_name)
        except:
            print("error")
    final = base + "FINAL" + ext
    for d in chan:
        final = final.replace(d, "")
    #ffmpeg
    print("ffmpeg işlemi için devam ? (y/n)")
    answer = input()
    try:
        if answer == "y":
            os.system(f"ffmpeg -i {fflist[0]} -i {fflist[1]} -c:v copy -c:a aac {final}")
    except:
        print("son.")
        
    
    
main()
