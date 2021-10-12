import picamera
import picamera.array
import time
import cv2

CascadeFile = "./haarcascades/haarcascade_frontalface_default.xml"

with picamera.PiCamera() as camera:

    # カメラのセッティング
    camera.resolution = (640, 480)
    camera.rotation = 180
    camera.start_preview()
    time.sleep(2)

    with picamera.array.PiRGBArray(camera) as stream:

        count = 0
        while True:

            # RGB映像データを格納
            camera.capture(stream, 'bgr', use_video_port=True)

            # グレースケールに変換
            gray = cv2.cvtColor(stream.array, cv2.COLOR_BGR2GRAY)

            # カスケードファイルを利用して顔の位置を見つける
            cascade = cv2.CascadeClassifier(CascadeFile)
            face_list = cascade.detectMultiScale(gray, minSize=(100, 100))

            timeString = time.strftime('%Y%m%d_%H%M%S')

            if len(face_list) > 0:
                for (x, y, w, h) in face_list:
                    print(timeString,"face_position:",count,x, y, w, h)

                    # 顔の周りに赤い線を引く
                    color = (0, 0, 255)
                    pen_w = 5
                    cv2.rectangle(stream.array, (x, y), (x+w, y+h), color, thickness = pen_w)

                    path = "./" + timeString + "_" + str(count) + ".jpg"
                    cv2.imwrite(path, stream.array)
                    path = "./" + timeString + "_" + str(count) + "_face.jpg"
                    dst = stream.array[y:y+h, x:x+w]
                    cv2.imwrite(path, dst)
            else:
                print(timeString,"face_position:",count,"none")

            # streamをリセット
            stream.seek(0)
            stream.truncate()

            count+=1

    camera.stop_preview()
