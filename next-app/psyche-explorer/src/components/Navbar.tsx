import Image from 'next/image'

export default function Navbar() {
    return (
        <nav className='flex justify-between p-5'>
            <div>
                <a href="#">Psyche Explorer</a>
            </div>
            <div>
                <a href="/about" className='px-8'>About</a>
                <a href="#">Github</a>
            </div>
        </nav>
    )
}