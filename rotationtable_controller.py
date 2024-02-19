from serial import Serial
from serial.tools import list_ports
from threading import Thread
from time import sleep


class RotationTableController():
    def __init__(self):
        self.port=''
        self.baud = 115200
        self.ser = None
        self.isConnect = False
        self.isStart=False
    
    def start(self):
        if self.isStart:return
        self.isStart=True
        Thread(target=self.connectin_loop,daemon=True).start()
    
    def end(self):
        if not self.isStart:return

        self.isStart=False

        if self.isConnect:
            self.ser.close()
            self.ser=None
            self.port=''
            self.isConnect=False

    #シリアルポートにコマンドを送って反応を見る
    def chk_connection(self,port:str):
        try:
            ser = Serial(port,self.baud,timeout=1.0,write_timeout=0.1,inter_byte_timeout=0.1)
            cmd='ping\r\n'#死活確認コマンド
            ser.write(cmd.encode())
            sleep(0.1)
            res = ser.read_all()
            ser.close()
            if res.decode().rsplit('\r\n')[1]=='True':
                return True
            else:
                return False
        except:
            return False
        
    #シリアルの接続監視
    #制御基板との接続を検出して自動接続する
    def connectin_loop(self):
        while self.isStart:
            #Comポートのリスト生成
            ports = list_ports.comports()
            devices = [info.device for info in ports]
            #print(devices)
            if self.isConnect:#切断されたポートがないかチェック
                sleep(0.1)
                if not self.port in devices:
                    print('disconnect',self.port)
                    self.port=''
                    self.isConnect=False
                else:
                    continue

            #それぞれのポートに接続してテーブル制御ポートを見つける
            for port in devices:
                if self.chk_connection(port):
                    self.port=port
                    break
            
            #接続
            if self.port != '':
                print('connect',self.port)
                self.ser = Serial(self.port,self.baud,timeout=1.0)
                self.isConnect=True


    #コマンド送信
    def send_cmd(self,cmd:str):
        #print(cmd)
        self.ser.reset_output_buffer()
        self.ser.reset_input_buffer()
        self.ser.write(cmd.encode())
        sleep(0.2)
        res = self.ser.read_all()
        #print(res)
        try:
            ret = eval(res.decode().rsplit('\r\n')[1])
        except:
            ret=False

        return ret
    

    #回転指令 指定した角度分テーブルを回転する
    #引数　回転角度[deg] 値をマイナスにすると逆回転
    #戻り値　正常:True 異常:False
    def rotate(self,deg:float):
        if not self.isConnect:
            return False      
        
        cmd = f'rot:{deg}\r\n'

        return self.send_cmd(cmd)

    #停止指令　テーブルの回転を即座に停止させる
    #戻り値　正常:True 異常:False
    def stop(self):
        if not self.isConnect:
            return False      
        
        cmd = 'stop\r\n'

        return self.send_cmd(cmd)

    #速度変更指令　テーブルの回転速度を変更する（テーブル回転中は変更不可）
    #引数　回転速度[Hz] 1~25000[Hz] 周波数が高いほど速度が速くなる
    #戻り値　正常:True 異常:False
    def set_speed(self,speed:int):
        if not self.isConnect:
            return False

        if 0>speed:
            return False
        
        speed_us = int(1/speed * 1000000)

        cmd = f'set_speed:{speed_us}\r\n'

        return self.send_cmd(cmd)

    #加速度変更　テーブルの回転加速度を変更する（テーブル回転中は変更不可）
    #引数　0で最大加速度、値を大きくすると加速度が小さくなり台形制御になる
    #戻り値　正常:True 異常:False
    def set_acc(self,acc:int):
        if not self.isConnect:
            return False
     
        cmd = f'set_acc:{acc}\r\n'
       
        return self.send_cmd(cmd)
    
    #移動ステータス　テーブルの動作状態を取得する　
    #戻り値　移動中:True 停止中/異常:False
    def get_status(self):
        if not self.isConnect:
            return False

        cmd = 'get_mov\r\n'
       
        return self.send_cmd(cmd)        
    
    #####以下開発用コマンドにつき通常は使用しない######
    #テーブル回転のパラメータ設定
    #引数 テーブル1回転のパルス数設定
    #戻り値　正常:True 異常:False
    def set_step_per_rev(self,step:int):
        if not self.isConnect:
            return False

        cmd = f'set_step:{step}\r\n'
       
        return self.send_cmd(cmd)

    #パルス出力ピン設定（設定後に再起動必要）
    #引数　pin番号(基板pin)：0(6), 1(5), 2(8), 3(10), 4(9), 6(4), 7(5), 26(0), 27(1), 28(2), 29(3)
    #戻り値　正常:True 異常:False
    def set_pin_config(self,pls_pin:int,dir_pin:int):
        if not self.isConnect:
            return False

        cmd = f'set_pin:{pls_pin},{dir_pin}\r\n'
       
        return self.send_cmd(cmd)    
