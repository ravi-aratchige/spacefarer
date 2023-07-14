import Image from 'next/image'
import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'
import { nanum_myeongjo } from './fonts'

export default function Home() {
  return (
    <main className="flex flex-col justify-between min-h-screen bg-[#0f041E] text-white">
      {/* Header (Navigation bar) */}
      <Navbar />
      
      {/* Hero section */}
      <section className='flex flex-col align-center text-center'>
        <div>
          <h1 className={`${nanum_myeongjo.className} text-6xl p-10`}>
            Discover the<br />Cosmic Secrets<br />of Your Soul
          </h1>
          <p className='p-5'>
            Psyche Explorer combines the worlds of astrology and computer science, using machine learning to help you discover the hidden depths of your personality.
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
