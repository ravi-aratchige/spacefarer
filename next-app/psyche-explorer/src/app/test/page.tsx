import Form from "@/components/Form";
import Footer from "@/components/Footer";
import Navbar from "@/components/Navbar";

export default function Test() {
    return (
        <main className='flex flex-col justify-between min-h-screen'>
            <Navbar />
            <Form />
            <Footer />
        </main>
    );
}