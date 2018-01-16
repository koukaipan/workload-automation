import time
from wlauto import ApkWorkload, Parameter
from wlauto.utils.android import adb_command

class TempleRun2(ApkWorkload):

    name = 'templerun2'
    description = "A racing game with various and repeatable scene"

    package = "com.imangi.templerun2"
    activity = "com.imangi.unityactivity.ImangiUnityProxyActivity"

    parameters = []

    loading_time = 30 # in sec
    def _skip_tutorial(self):
        # wait 'launch_loading_timeout' sec for loading, then enter tutorial
        self.logger.debug('Waiting for the game to load (1st run)...')
        time.sleep(self.loading_time)

        self.device.execute("input keyevent 3", 20)
        time.sleep(5)

        self.device.execute('am force-stop {}'.format(self.package))
        time.sleep(5)
        self.logger.debug('Tutorial is completed...')


    def _execute(self):
        # We start game here, because any operation in run() will be measured.
        self.launch_application()
        self.logger.debug('Waiting for the game to load (normal run)...')
        time.sleep(self.loading_time)
        self.device.execute("input tap 550 1200", 20)
        self.logger.debug('The game starts running.')
        time.sleep(5)


    def setup(self, context):
        super(TempleRun2, self).setup(context)
        # We do a 1st run here and skip the tutorial
        self._skip_tutorial()
        self.kill_background()
        self.device.clear_logcat()
        self._execute()


    # do nothing here, any operation in this method will be measured.
    def run(self, context):
        time.sleep(10)


    def validate(self):
        pass
