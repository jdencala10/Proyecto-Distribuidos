namespace py theGifServer

struct Gif{
    1: i32 id,
    2: string url,
    3: i32 contador,
    4: string descripcion 
} 

service losMejoresGifs {

    list<Gif> top10(),

    list<Gif> top10ConCache(),

    Gif yoTeInvoco( 1: string nombreGif )

}
