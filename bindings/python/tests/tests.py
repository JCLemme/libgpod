import datetime
import importlib
import importlib.util
import os
import shutil
import tempfile
import sys
import time
import types
import unittest

resource_dir = os.environ["RESOURCE_DIR"]
gpod_init = os.environ["GPOD_INIT"]

# load gpod.py first
gpod_gpod = importlib.import_module('gpod')
sys.modules["gpod.gpod"] = gpod_gpod
# then load the actual gpod module
spec = importlib.util.spec_from_file_location("gpod", gpod_init)
gpod = importlib.util.module_from_spec(spec)
sys.modules["gpod"] = gpod
spec.loader.exec_module(gpod)


class TestiPodFunctions(unittest.TestCase):
    def setUp(self):
        self.mp = tempfile.mkdtemp()
        control_dir = os.path.join(self.mp, 'iPod_Control')
        music_dir = os.path.join(control_dir, 'Music')
        shutil.copytree(resource_dir,
                        control_dir)
        os.mkdir(music_dir)
        for i in range(20):
            os.mkdir(os.path.join(music_dir, "f%02d" % i))
        self.db = gpod.Database(self.mp)

    def tearDown(self):
        shutil.rmtree(self.mp)

    def testClose(self):
        self.db.close()

    def testListPlaylists(self):
        playlists = set([p.name for p in self.db.Playlists])
        self.assertSetEqual({'Nicks iPod', 'Podcasts'}, playlists)

    def testCreatePlaylist(self):
        self.assertEqual(len(self.db.Playlists), 2)
        _ = self.db.new_Playlist('my title')
        self.assertEqual(len(self.db.Playlists), 3)

    def testPopulatePlaylist(self):
        trackname = os.path.join(self.mp,
                                 'iPod_Control',
                                 'tiny.mp3')

        pl = self.db.new_Playlist('my title')
        self.assertEqual(len(pl), 0)
        t = self.db.new_Track(filename=trackname)
        pl.add(t)
        self.assertEqual(len(pl), 1)

    def testAddTrack(self):
        trackname = os.path.join(self.mp,
                                 'iPod_Control',
                                 'tiny.mp3')
        for n in range(1, 5):
            _ = self.db.new_Track(filename=trackname)
            self.assertEqual(len(self.db), n)
        self.db.copy_delayed_files()
        for track in self.db:
            self.assertTrue(os.path.exists(track.ipod_filename()))

    def testAddRemoveTrack(self):
        self.testAddTrack()
        for n in range(4, 0, -1):
            track = self.db[0]
            track_file = track.ipod_filename()
            self.assertEqual(len(self.db), n)
            self.db.remove(track, ipod=True, quiet=True)
            self.failIf(os.path.exists(track_file))

    def testDatestampSetting(self):
        trackname = os.path.join(self.mp,
                                 'iPod_Control',
                                 'tiny.mp3')
        t = self.db.new_Track(filename=trackname)
        date = datetime.datetime.now()
        t['time_added'] = date
        self.assertEqual(date.year, t['time_added'].year)
        self.assertEqual(date.second, t['time_added'].second)
        # microsecond won't match, that's lost in the itdb
        date = datetime.datetime.now()
        t['time_added'] = time.mktime(date.timetuple())
        self.assertEqual(date.year, t['time_added'].year)
        self.assertEqual(date.second, t['time_added'].second)

    def testTrackContainerMethods(self):
        self.testAddTrack()
        track = self.db[0]
        self.assertTrue('title' in track)

    def testVersion(self):
        self.assertEqual(type(gpod.version_info),
                         types.TupleType)


class TestPhotoDatabase(unittest.TestCase):
    def setUp(self):
        self.mp = tempfile.mkdtemp()
        control_dir = os.path.join(self.mp, 'iPod_Control')
        photo_dir = os.path.join(control_dir, 'Photos')
        shutil.copytree(resource_dir,
                        control_dir)
        os.mkdir(photo_dir)
        self.db = gpod.PhotoDatabase(self.mp)
        gpod.itdb_device_set_sysinfo(self.db._itdb.device,
                                     "ModelNumStr",
                                     "MA450")

    def tearDown(self):
        shutil.rmtree(self.mp)

    def testClose(self):
        self.db.close()

    def testAddPhotoAlbum(self):
        """ Test adding 5 photo albums to the database """
        for i in range(0, 5):
            count = len(self.db.PhotoAlbums)
            _ = self.db.new_PhotoAlbum(title="Test %s" % i)
            self.assertTrue(len(self.db.PhotoAlbums) == (count + 1))

    def testAddRemovePhotoAlbum(self):
        """ Test removing all albums but "Photo Library" """
        self.testAddPhotoAlbum()
        pas = [x for x in self.db.PhotoAlbums if x.name != "Photo Library"]
        for pa in pas:
            self.db.remove(pa)
        self.assertEqual(len(self.db.PhotoAlbums), 1)

    def testRenamePhotoAlbum(self):
        bad = []
        good = []

        self.testAddPhotoAlbum()
        pas = [x for x in self.db.PhotoAlbums if x.name != "Photo Library"]
        for pa in pas:
            bad.append(pa.name)
            pa.name = "%s (renamed)" % pa.name
            good.append(pa.name)

        pas = [x for x in self.db.PhotoAlbums if x.name != "Photo Library"]
        for pa in pas:
            self.assertTrue(pa.name in bad)
            self.assertTrue(pa.name not in good)

    def testEnumeratePhotoAlbums(self):
        [photo for photo in self.db.PhotoAlbums]

    def testAddPhoto(self):
        photoname = os.path.join(self.mp,
                                 'iPod_Control',
                                 'tiny.png')
        self.assertTrue(os.path.exists(photoname))
        for n in range(1, 5):
            _ = self.db.new_Photo(filename=photoname)
            self.assertEqual(len(self.db), n)

    def testAddPhotoToAlbum(self):
        self.testAddPhoto()
        pa = self.db.new_PhotoAlbum(title="Add To Album Test")
        count = len(pa)
        for p in self.db.PhotoAlbums[0]:
            pa.add(p)
        self.assertEqual(len(pa), len(self.db.PhotoAlbums[0]))
        self.assertTrue(len(pa) > count)

    def testRemovePhotoFromAlbum(self):
        self.testAddPhotoToAlbum()
        pa = self.db.PhotoAlbums[1]
        for p in pa[:]:
            pa.remove(p)
        # make sure we didn't delete the photo
        self.assertTrue(len(self.db.PhotoAlbums[0]) > 0)
        # but that we did remove them from album
        self.assertEqual(len(pa), 0)

    def testAddRemovePhoto(self):
        self.testAddPhoto()
        self.assertTrue(len(self.db) > 0)
        for photo in self.db.PhotoAlbums[0][:]:
            self.db.remove(photo)
        self.assertEqual(len(self.db), 0)

    def testAddCountPhotos(self):
        count = len(self.db)
        self.testAddPhoto()
        self.assertTrue(len(self.db) > count)

    def testEnumeratePhotos(self):
        for album in self.db.PhotoAlbums:
            [photo for photo in album]

    def testPhotoContainerMethods(self):
        self.testAddPhoto()
        photo = self.db[0]
        self.assertTrue('id' in photo)


if __name__ == '__main__':
    unittest.main()
