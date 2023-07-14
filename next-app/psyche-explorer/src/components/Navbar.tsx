import { Anek_Devanagari } from 'next/font/google'
import Image from 'next/image'

export default function Navbar() {
    return (
        <nav className='flex justify-between p-5'>
            <div>Psyche Explorer</div>
            <div>
                <a href="#" className='px-8'>About</a>
                <a href="#">Github</a>
            </div>
        </nav>
    )
}