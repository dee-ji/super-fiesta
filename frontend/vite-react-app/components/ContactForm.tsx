// ContactForm.tsx
import React, { useState } from 'react';
import axios from 'axios';
import './ContactForm.css';

interface ContactFormState {
  name: string;
  email: string;
  message: string;
}

const ContactForm: React.FC = () => {
  const [formData, setFormData] = useState<ContactFormState>({ name: '', email: '', message: '' });
  const [errors, setErrors] = useState<ContactFormState>({ name: '', email: '', message: '' });

  const validateEmail = (email: string) => {
    return /\S+@\S+\.\S+/.test(email);
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });

    // Real-time validation example
    if (name === 'email' && !validateEmail(value)) {
      setErrors({ ...errors, email: 'Invalid email address' });
    } else {
      setErrors({ ...errors, [name]: '' });
    }
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (!errors.name && !errors.email && !errors.message) {
      try {
        await axios.post('http://localhost:8000/contact/', formData);
        alert('Message sent successfully');
        setFormData({ name: '', email: '', message: '' }); // Reset form
      } catch (error) {
        console.error('There was an error sending the message', error);
      }
    }
  };

  return (
    <div className="contact-form-container">
        <form className="contact-form" onSubmit={handleSubmit}>
        <div>
            <label>Name</label>
            <input type="text" name="name" value={formData.name} onChange={handleChange} />
            {errors.name && <p>{errors.name}</p>}
        </div>
        <div>
            <label>Email</label>
            <input type="email" name="email" value={formData.email} onChange={handleChange} />
            {errors.email && <p>{errors.email}</p>}
        </div>
        <div>
            <label>Message</label>
            <textarea name="message" value={formData.message} onChange={handleChange}></textarea>
            {errors.message && <p>{errors.message}</p>}
        </div>
        <button type="submit">Send</button>
        </form>
    </div>
  );
};

export default ContactForm;
