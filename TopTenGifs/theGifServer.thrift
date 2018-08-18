namespace py theGifServer

struct Gif{
    1: i32 id,
    2: string nombre,
    3: i32 contador 
} 

service losMejoresGifs {

    list<Gif> top10(),

    Gif yoTeInvoco( 1: string nombreGif )

}
