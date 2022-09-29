from music_playlist import Track, MediaPlayerQueue

if __name__ == '__main__':
    track1 = Track("Song1")
    track2 = Track("Song 2")
    track3 = Track("Song 3")

    media_player = MediaPlayerQueue()

    media_player.add_track(track1)
    media_player.add_track(track2)
    media_player.add_track(track3)

    media_player.play()
