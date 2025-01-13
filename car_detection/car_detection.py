import cv2

def detect_cars(video_path):
    video= cv2.VideoCapture(video_path)
    back_sub = cv2.createBackgroundSubtractorMOG2()

    while True:
        success, frame = video.read()

        if not success:
            print("video finished or can not read video. ")
            break

        frame = cv2.resize(frame,(640,360))
        mask = back_sub.apply(frame)
        mask = cv2.medianBlur(mask,5)
        contours, _ = cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                
                cv2.rectangle(frame,(x,y ),(x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("car detection", frame) 
        cv2.imshow("moving objects", mask)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_file = "c:\\Users\\nav\\Downloads\\sample_video.mp4"
    detect_cars(video_file)

