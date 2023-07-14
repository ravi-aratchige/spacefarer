// import Head from 'next/head'
import Image from 'next/image'
import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'
import { Nanum_Myeongjo } from 'next/font/google'

const nanum_myeongjo = Nanum_Myeongjo({
  subsets: ['latin'],
  weight: ['400', '700', '800']
});

export default function Home() {
  return (
    <main className="flex flex-col justify-between min-h-screen bg-[#0f041E] text-white">
      {/* Header (Navigation bar) */}
      <Navbar />
      
      {/* Hero section */}
      <section className='flex flex-col align-center text-center'>
        <div>
          <h1 className='text-6xl font-nanum-myeongjo'>
            Discover the<br />Cosmic Secrets<br />of Your Soul
          </h1>
          <p className='p-5'>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Sed ut quam dapibus, tempor est nec, consequat velit.
          </p>
          <button className="bg-violet-600 hover:bg-violet-400 text-white font-bold py-2 px-4 rounded">
            Take the Test
          </button>
        </div>
      </section>

      {/* Footer */}
      <Footer />
    </main>
  )
}
