import numpy as np

def throw_rock(m, v0, theta_deg):
    g = 9.81
    # Açıyı dereceyi radyana çevirmek için numpy kullanıldı
    theta_rad = np.radians(theta_deg)

    # DÜZELTİLMİŞ FİZİKSEL HESAPLAMALAR
    tf = (2 * v0 * np.sin(theta_rad)) / g
    R = (v0**2 * np.sin(2 * theta_rad)) / g
    # Maksimum Yükseklik (hm) Formülü düzeltildi
    hm = (v0**2 * (np.sin(theta_rad)**2)) / (2 * g)
    vh = v0 * np.cos(theta_rad)
    # Kinetik Enerji (kh) Formülü düzeltildi (K = 0.5 * m * vh^2)
    kh = 0.5 * m * vh**2

    # TESTİ GEÇMEK İÇİN ÇIKTI FORMATI AYARLAMASI (Boşluklara DİKKAT!)
    # Not: np.pi yerine theta_deg kullanıldığı için np.degrees(theta_rad) kaldırıldı.
    print(f"For a rock with {m:.3f} kg mass thrown with {v0:.3f} m/s at an angle of {theta_deg: 5.2f} degrees:")
    
    # "is" kelimesinden sonra 4 boşluk bırakılarak çıktı formatı eşleştirildi.
    print(f"Time of flight is    {tf:.2e} s")
    print(f"The range in x-direction is    {R:.2e} m")
    print(f"Maximum height is    {hm:.2e} m")
    print(f"The speed at maximum height is    {vh:.2e} m/s")
    print(f"Kinetic energy at the maximum height is {kh:.2e} J")
    
    return tf, R, hm, vh, kh
